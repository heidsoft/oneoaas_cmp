# -*- coding: utf-8 -*-

from pygments.styles import vim
from pyvim.connect import SmartConnectNoSSL
from pyVmomi import vim, vmodl
#
# def WaitForTasks(tasks, si):
#     """
#     Given the service instance si and tasks, it returns after all the
#     tasks are complete
#     """
#
#     pc = si.content.propertyCollector
#
#     taskList = [str(task) for task in tasks]
#
#     # Create filter
#     objSpecs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
#                 for task in tasks]
#     propSpec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
#                                                           pathSet=[], all=True)
#     filterSpec = vmodl.query.PropertyCollector.FilterSpec()
#     filterSpec.objectSet = objSpecs
#     filterSpec.propSet = [propSpec]
#     filter = pc.CreateFilter(filterSpec, True)
#
#     try:
#         version, state = None, None
#
#         # Loop looking for updates till the state moves to a completed state.
#         while len(taskList):
#             update = pc.WaitForUpdates(version)
#             for filterSet in update.filterSet:
#                 for objSet in filterSet.objectSet:
#                     task = objSet.obj
#                     for change in objSet.changeSet:
#                         if change.name == 'info':
#                             state = change.val.state
#                         elif change.name == 'info.state':
#                             state = change.val
#                         else:
#                             continue
#
#                         if not str(task) in taskList:
#                             continue
#
#                         if state == vim.TaskInfo.State.success:
#                             # Remove task from taskList
#                             taskList.remove(str(task))
#                         elif state == vim.TaskInfo.State.error:
#                             raise task.info.error
#             # Move to next version
#             version = update.version
#     finally:
#         if filter:
#             filter.Destroy()


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
    def stop(self):
        pass

    #重启
    def reboot(self,vmnames):
        content = self.client.content
        objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                         [vim.VirtualMachine],
                                                         True)
        vmList = objView.view
        objView.Destroy()

        # Find the vm and power it on
        tasks = [vm.PowerOn() for vm in vmList if vm.name in vmnames]

        # WaitForTasks(tasks=tasks,si=self.client)
        pass

