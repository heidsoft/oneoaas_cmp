#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
function:vcenter manage

"""
import time
from pygments.styles import vim
from pyvim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim, vmodl

from common.log import logger

"""
打印虚拟机对象
"""
def PrintVmInfo(vm, depth=1):
    """
    Print information for a particular virtual machine or recurse into a folder
    or vApp with depth protection
    """
    maxdepth = 10

    # if this is a group it will have children. if it does, recurse into them
    # and then return
    if hasattr(vm, 'childEntity'):
        if depth > maxdepth:
            return
        vmList = vm.childEntity
        for c in vmList:
            PrintVmInfo(c, depth+1)
        return

    # if this is a vApp, it likely contains child VMs
    # (vApps can nest vApps, but it is hardly a common usecase, so ignore that)
    if isinstance(vm, vim.VirtualApp):
        vmList = vm.vm
        for c in vmList:
            PrintVmInfo(c, depth + 1)
        return

    summary = vm.summary
    print("Name       : ", summary.config.name)
    print("Path       : ", summary.config.vmPathName)
    print("Guest      : ", summary.config.guestFullName)
    annotation = summary.config.annotation
    if annotation != None and annotation != "":
        print("Annotation : ", annotation)
    print("State      : ", summary.runtime.powerState)
    if summary.guest != None:
        ip = summary.guest.ipAddress
        if ip != None and ip != "":
            print("IP         : ", ip)
    if summary.runtime.question != None:
        print("Question  : ", summary.runtime.question.text)
    print("")

class VmManage(object):

    def __init__(self,host,user,password,port,ssl):
        self.host = host
        self.user = user
        self.pwd = password
        self.port = port
        self.sslContext = ssl
        self.client = SmartConnectNoSSL(host=host,
                                      user=user,
                                      pwd=password,
                                      port=int(port)
                                    )

        if not self.client:
           raise Exception("构建虚拟机管理器失败")

    #根据资源类型和名称，获取资源对象
    def _get_obj(self,content, vimtype, name):
        """
        Get the vsphere object associated with a given text name
        """
        obj = None
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def _get_all_objs(self,content, vimtype):
        """
        Get all the vsphere objects associated with a given type
        """
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for c in container.view:
            obj.update({c: c.name})
        return obj


    def login_in_guest(self,username, password):
        return vim.vm.guest.NamePasswordAuthentication(username=username,password=password)

    def start_process(self,si, vm, auth, program_path, args=None, env=None, cwd=None):
        cmdspec = vim.vm.guest.ProcessManager.ProgramSpec(arguments=args, programPath=program_path, envVariables=env, workingDirectory=cwd)
        cmdpid = si.content.guestOperationsManager.processManager.StartProgramInGuest(vm=vm, auth=auth, spec=cmdspec)
        return cmdpid

    def is_ready(self,vm):

        while True:
            system_ready = vm.guest.guestOperationsReady
            system_state = vm.guest.guestState
            system_uptime = vm.summary.quickStats.uptimeSeconds
            if system_ready and system_state == 'running' and system_uptime > 90:
                break
            time.sleep(10)

    def get_vm_by_name(self,si, name):
        """
        Find a virtual machine by it's name and return it
        """
        return self._get_obj(si.RetrieveContent(), [vim.VirtualMachine], name)

    def get_host_by_name(self,si, name):
        """
        Find a virtual machine by it's name and return it
        """
        return self._get_obj(si.RetrieveContent(), [vim.HostSystem], name)

    def get_resource_pool(self,si, name):
        """
        Find a virtual machine by it's name and return it
        """
        return self._get_obj(si.RetrieveContent(), [vim.ResourcePool], name)

    def get_resource_pools(self,si):
        """
        Returns all resource pools
        """
        return self._get_all_objs(si.RetrieveContent(), [vim.ResourcePool])

    def get_datastores(self,si):
        """
        Returns all datastores
        """
        return self._get_all_objs(si.RetrieveContent(), [vim.Datastore])

    def get_hosts(self,si):
        """
        Returns all hosts
        """
        return self._get_all_objs(si.RetrieveContent(), [vim.HostSystem])

    def get_datacenters(self,si):
        """
        Returns all datacenters
        """
        return self._get_all_objs(si.RetrieveContent(), [vim.Datacenter])

    def get_registered_vms(self,si):
        """
        Returns all vms
        """
        return self._get_all_objs(si.RetrieveContent(), [vim.VirtualMachine])


    #获取虚拟机列表
    def list(self):
        content = self.client.content
        objView = content.viewManager.CreateContainerView(content.rootFolder,[vim.VirtualMachine],True)
        vmList = objView.view
        # vmAllList = []
        # content = self.client.RetrieveContent()
        # for child in content.rootFolder.childEntity:
        #     if hasattr(child, 'vmFolder'):
        #         datacenter = child
        #         vmFolder = datacenter.vmFolder
        #         vmList = vmFolder.childEntity
        #         vmAllList.append(vmList)

        return vmList


    #创建
    def create(self):

        pass

    #关闭
    def stop(self,vmnames):
        print 'vm manage stop...'
        content = self.client.content
        objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objView.view
        objView.Destroy()

        # Find the vm and power it on
        tasks = [vm.PowerOff() for vm in vmList if vm.name in vmnames]

        from pyvim.task import WaitForTasks
        WaitForTasks(tasks=tasks,si=self.client)

    #开启
    def start(self,vmnames):
        print 'vm manage start...'
        # content = self.client.content
        # objView = content.viewManager.CreateContainerView(content.rootFolder,
        #                                                   [vim.VirtualMachine],
        #                                                   True)
        # vmList = objView.view
        # objView.Destroy()


        # tasks = [vm.PowerOn() for vm in vmList if vm.name in vmnames]
        #
        # print tasks
        #
        # from pyvim.task import WaitForTasks
        # WaitForTasks(tasks=tasks,si=self.client)

        vm = self.get_vm_by_name(self.client, vmnames)
        try:
            print "find vm and start vm ..."
            vm.PowerOnGuest()
        except:
            # forceably shutoff/on
            # need to do if vmware guestadditions isn't running
            vm.ResetVM_Task()

        Disconnect(self.client)


    #重启
    def reboot(self,vmnames):
        print 'vm manage reboot...'
        vm = self.get_vm_by_name(self.client, vmnames)
        try:
            vm.RebootGuest()
        except:
            # forceably shutoff/on
            # need to do if vmware guestadditions isn't running
            vm.ResetVM_Task()

        Disconnect(self.client)


