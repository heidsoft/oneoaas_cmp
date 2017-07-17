# -*- coding: utf-8 -*-
import random

import gevent
import pyVmomi
import simplejson as simplejson
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from gevent import Greenlet
from pyVmomi.VmomiSupport import DataObject

from blueking.component.base import logger
from common.mymako import render_mako_context, render_json
from home_application.celery_tasks import execute_task
from home_application.models import VcenterAccount, VcenterVirtualMachine
from home_application.vmware.vmware_object import VirtualMachine
from hybirdsdk.virtualMachine import VmManage
from pyVmomi import vim, vmodl

"""
虚拟机
"""
def getVmManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/vm_manage.html'
    )

"""
虚拟机配置
"""
def getVmConfigView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_config.html'
    )

"""
集群管理
"""
def getClusterManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/cluster_manage.html'
    )

"""
数据中心管理
"""
def getDatacenterManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/datacenter_manage.html'
    )

"""
部门管理
"""
def getDepartmentManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/department_manage.html'
    )

"""
部门资源管理
"""
def getDepartmentResourceManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/department_resource_manage.html'
    )

"""
监控配置
"""
def getMonitorConfigView(request):
    return render_mako_context(
        request, '/home_application/vmware/monitor_config.html'
    )

"""
用户管理
"""
def getUserManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/user_manage.html'
    )


"""
存储管理
"""
def getStorageManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/storage_manage.html'
    )



"""

创建vcenter账号

"""
def createVCenterAccount(request):
    try:
        if request.method == 'POST':
            accountName = request.POST['accountName']
            accountPassword = request.POST['accountPassword']
            vcenterHost = request.POST['vcenterHost']
            vcenterPort = request.POST['vcenterPort']
            vcenterVersion = request.POST['vcenterVersion']

            account = VcenterAccount(account_name=accountName,
                                     account_password=accountPassword,
                                     vcenter_host=vcenterHost,
                                     vcenter_port=vcenterPort,
                                     vcenter_version=vcenterVersion)
            result = account.save()
            print request

        res = {
            'result': True,
            'message': "添加成功",
        }
    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)


def createVcenterVirtualMachine(vm,depth=1):

    maxdepth = 10

    # if this is a group it will have children. if it does, recurse into them
    # and then return
    if hasattr(vm, 'childEntity'):
        if depth > maxdepth:
            return None
        vmList = vm.childEntity
        for c in vmList:
            createVcenterVirtualMachine(c, depth+1)
        return None

    # if this is a vApp, it likely contains child VMs
    # (vApps can nest vApps, but it is hardly a common usecase, so ignore that)
    if isinstance(vm, vim.VirtualApp):
        vmList = vm.vm
        for c in vmList:
            createVcenterVirtualMachine(c, depth + 1)
        return None

    vcenterVirtualMachineModel = VcenterVirtualMachine()
    summary = vm.summary
    vcenterVirtualMachineModel.name = summary.config.name
    vcenterVirtualMachineModel.vm_pathname = summary.config.vmPathName
    vcenterVirtualMachineModel.guest_fullname = summary.config.guestFullName
    vcenterVirtualMachineModel.power_state = summary.runtime.powerState


    if summary.guest != None:
        ip = summary.guest.ipAddress
        if ip != None and ip != "":
            vcenterVirtualMachineModel.ipaddress = ip
    else:
        vcenterVirtualMachineModel.ipaddress=""
    return vcenterVirtualMachineModel

#同步账号
def syncVCenterAccount(request):
    if request.method == 'POST':
        accountId = request.POST['id']

        print accountId

        accountModel = VcenterAccount.objects.get(id=accountId)

        print accountModel

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    vmAllList = vmManager.list()

    if vmAllList is None:
        res = {
            'result': True,
            'message': "同步成功,Vcenter没有虚拟机",
        }
    else:
        for vm in vmAllList:
            vmTempModel =  createVcenterVirtualMachine(vm)
            if vmTempModel != None and isinstance(vmTempModel,VcenterVirtualMachine):
                vmTempModel.account = accountModel
                vmTempModel.save()

        res = {
            'result': True,
            'message': "同步成功",
        }

    return render_json(res)

#查询vcenter账号配置
def getVcenterAccountList(request):
    logger.info("查询配置vcenter配置")

    accountObjectList = VcenterAccount.objects.all()
    accountJsonList = []
    from django.forms.models import model_to_dict
    for account in accountObjectList:
        tempAccount = model_to_dict(account)
        accountJsonList.append(tempAccount)

    res = {
        "recordsTotal": len(accountObjectList),
        'data': accountJsonList
    }

    return render_json(res)

#写入文件
def WriteFile(filename="test",content=""):
    fo = open(filename, "wb")
    fo.write( content )
    fo.close()


#获取虚拟机列表
def getVcenterVirtualMachineList(request):
    logger.info("查询配置vcenter 虚拟机")

    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    # vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    # vmAllList = vmManager.list()
    #
    # for vm in vmAllList:
    #     if vm is not None and isinstance(vm, vim.VirtualMachine):
    #         my =  VirtualMachine()
    #         my.host = str( vm.summary.runtime.host)
    #         my.connectionState = str(vm.summary.runtime.connectionState)
    #         my.powerState = str(vm.summary.runtime.powerState)
            #print my.toJSON()


    vcenterVirtualMachineObjectList = VcenterVirtualMachine.objects.all()
    vmJsonList = []
    from django.forms.models import model_to_dict
    for vm in vcenterVirtualMachineObjectList:
        tempvm = model_to_dict(vm)
        vmJsonList.append(tempvm)

    res = {
        "recordsTotal": len(vmJsonList),
        "page": 1,
        "pages": 6,
        "start": 10,
        "end": 20,
        "length": 10,
        'data': vmJsonList
    }

    return render_json(res)



#关机
def poweroffVmRequest(request):
    logger.info("关闭虚拟机")
    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            print 'vmid is %s ' % vmId
            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = vcenterVirtualMachineModel.account
            print accountModel

        if accountModel is None:
            res = {
                'result': True,
                'message': u"关机失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
            result = vmManager.stop(vcenterVirtualMachineModel.name)
            print result
            res = {
                'result': True,
                'message': u"关机成功",
            }

    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)

#开启
def startVmRequest(request):
    logger.info("开启虚拟机")
    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            print 'vmid is %s ' % vmId
            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = vcenterVirtualMachineModel.account
            print accountModel.account_name

        if accountModel is None:
            res = {
                'result': True,
                'message': u"开启失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)

            result = vmManager.start(vcenterVirtualMachineModel.name)
            print result
            res = {
                'result': True,
                'message': u"开启成功",
            }
    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }

    return render_json(res)

#重启
def rebootVmRequest(request):
    logger.info("重启虚拟机")
    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            print 'vmid is %s ' % vmId

            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = vcenterVirtualMachineModel.account
            print accountModel

        if accountModel is None:
            res = {
                'result': True,
                'message': u"重启失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)

            result = vmManager.reboot(vcenterVirtualMachineModel.name)

            if result is None:
                res = {
                    'result': True,
                    'message': u"重启成功",
                }
            else:
                res = {
                    'result': True,
                    'message': u"重启失败",
                }



    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)


#销毁
def destroyVmRequest(request):
    logger.info("销毁虚拟机")
    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = vcenterVirtualMachineModel.account
            print accountModel

        if accountModel is None:
            res = {
                'result': True,
                'message': u"销毁失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)

            #todo 销毁
            res = {
                'result': True,
                'message': u"销毁成功",
            }

    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)

#获取蓝鲸cmdb 业务配置信息
def getAppList(request):
    from blueking.component.shortcuts import get_client_by_request
    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    from conf import  default
    kwargs = {'app_id': default.APP_ID,'app_secret':default.APP_TOKEN}
    apps = client.cc.get_app_list(kwargs)
    results = {}
    appList = []
    if isinstance(apps,dict):
        appArray = apps['data']
        for app in appArray:
            appList.append({'id':app['ApplicationID'],'text':app['ApplicationName']})

        results['results']=appList
    else:
        results['results']=appList
    return render_json(results)


#创建虚拟机
def createVmRequest(request):
    pass

#克隆虚拟机
def cloneVmRequest(request):
    logger.info("克隆虚拟机")
    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            vmName = request.POST['vmName']
            vmDatacenter = request.POST['vmDatacenter']
            vmCluster = request.POST['vmCluster']
            vmDatastore = request.POST['vmDatastore']

            print 'vmid is %s, vmName is %s , vmDatacenter is %s, vmCluster is %s, vmDatastore is %s '.format(vmId,vmName,vmDatacenter,vmCluster,vmDatastore)
            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = vcenterVirtualMachineModel.account

        if accountModel is None:
            res = {
                'result': True,
                'message': u"克隆失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)

            template = vmManager.get_vm_by_name(vcenterVirtualMachineModel.name)
            print template
            result = vmManager.clone(template=template,
                                     vm_name=vmName,
                                     datacenter_name=vmDatacenter,
                                     vm_folder=None,
                                     datastore_name=vmDatastore,
                                     cluster_name=vmCluster,
                                     resource_pool=None,
                                     power_on=True)

            if result is None:
                res = {
                    'result': True,
                    'message': u"克隆成功",
                }
            else:
                res = {
                    'result': True,
                    'message': u"克隆失败",
                }
    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)

#打开webssh
def WebSSHVmRequest(request):
    pass

#获取所有数据中心
def getAllDatacenterRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    allDatacenter = vmManager.get_datacenters()

    results = {}

    datacenterList = []
    if isinstance(allDatacenter,dict):
        for datacenter in allDatacenter:
            # print datacenter.__str__
            # print datacenter.__dict__
            # print datacenter._stub
            # print datacenter._moId
            datacenterList.append({'id':datacenter.name,'text':datacenter.name})
        results['results']=datacenterList
    else:
        results['results']=datacenterList
    return render_json(results)


#获取所有集群
def getAllClusterRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    allCluster = vmManager.get_cluster_pools()
    print allCluster

    results = {}
    clusterList = []
    if allCluster is not None:
        for cluster in allCluster:
            print cluster
            clusterList.append({'id':cluster.name,'text':cluster.name})

        results['results']=clusterList
    else:
        results['results']=clusterList
    return render_json(results)

#获取数据中心所有的集群
def getClusterByDatacenterRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    allDatacenter = vmManager.get_datacenters()

    results = {}
    datacenterList = []
    if isinstance(allDatacenter,dict):
        for datacenter in allDatacenter:
            datacenterList.append({'id':"1",'text':'1'})

        results['results']=datacenterList
    else:
        results['results']=datacenterList
    return render_json(results)

#获取存储
def getAllDatastoreRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    allDatastore = vmManager.get_datastores()

    results = {}
    datastoreList = []
    if isinstance(allDatastore,dict):
        for datastore in allDatastore:
            datastoreList.append({'id':datastore.name,'text':datastore.name})

        results['results']=datastoreList
    else:
        results['results']=datastoreList
    return render_json(results)







########################################test request
"""
并发测试
"""
def asyncDemo(request):
    logger.info("测试异步任务 开始")
    execute_task()
    logger.info("测试异步任务 结束")
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])


    #同步执行
    synchronous()

    #异步执行
    asynchronous()


    res = {
        'result': True,
        'message': "成功",
    }
    return render_json(res)

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

#同步执行
def synchronous():
    for i in range(1,10):
        task(i)

#异步执行
def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)


"""
定义Greenlet的子类，可以设定任务消息
g = MyGreenlet("Hi there!", 3)
g.start()
g.join()
"""
class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)
