# -*- coding: utf-8 -*-

from pyVim.connect import SmartConnect, Disconnect
from pygments.styles import vim
from pyVmomi import vim, vmodl

def WaitForTasks(tasks, si):
    """
    Given the service instance si and tasks, it returns after all the
    tasks are complete
    """

    pc = si.content.propertyCollector

    taskList = [str(task) for task in tasks]

    # Create filter
    objSpecs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
                for task in tasks]
    propSpec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                          pathSet=[], all=True)
    filterSpec = vmodl.query.PropertyCollector.FilterSpec()
    filterSpec.objectSet = objSpecs
    filterSpec.propSet = [propSpec]
    filter = pc.CreateFilter(filterSpec, True)

    try:
        version, state = None, None

        # Loop looking for updates till the state moves to a completed state.
        while len(taskList):
            update = pc.WaitForUpdates(version)
            for filterSet in update.filterSet:
                for objSet in filterSet.objectSet:
                    task = objSet.obj
                    for change in objSet.changeSet:
                        if change.name == 'info':
                            state = change.val.state
                        elif change.name == 'info.state':
                            state = change.val
                        else:
                            continue

                        if not str(task) in taskList:
                            continue

                        if state == vim.TaskInfo.State.success:
                            # Remove task from taskList
                            taskList.remove(str(task))
                        elif state == vim.TaskInfo.State.error:
                            raise task.info.error
            # Move to next version
            version = update.version
    finally:
        if filter:
            filter.Destroy()

class ManageVm(object):

    def __init__(self,host,user,password,port,ssl):
        self.host = host
        self.user = user
        self.pwd = password
        self.port = port
        self.sslContext = ssl
        self.client = SmartConnect(host=host,
                                      user=user,
                                      pwd=password,
                                      port=int(port),
                                      sslContext=ssl)

        if not self.client:
           raise Exception("构建虚拟机管理器失败")

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

        WaitForTasks(tasks=tasks,si=self.client)
        pass
