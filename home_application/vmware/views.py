# -*- coding: utf-8 -*-
import random
import traceback

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
from home_application.models import *
from home_application.vmware.object_convert import convertVmEntityToVcenterVirtualMachine
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
            accountList =  VcenterAccount.objects.all()
            #判断是否有账号
            if len(accountList) == 0:
                result = account.save()
                res = {
                    'result': True,
                    'message': "保存账号成功",
                }
            else:
                accountExist = VcenterAccount.objects.get(account_name=accountName)
                if accountExist is not None:
                    res = {
                        'result': True,
                        'message': "账号已经存在",
                    }
                else:
                    result = account.save()
                    res = {
                        'result': True,
                        'message': "保存账号成功",
                    }

    except Exception as e:
        res = {
            'result': False,
            'message': e.message,
        }
    return render_json(res)




#同步账号
def syncVCenterAccount(request):
    accountId = None
    if request.method == 'POST':
        accountId = request.POST['id']
        print "accountId is %s" % accountId
        if accountId is None or accountId <0:
            res = {
                'result': True,
                'message': "该账号不存在",
            }
            return render_json(res)

    accountModel = VcenterAccount.objects.get(id=accountId)
    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    rootFolder = vmManager.content.rootFolder

    try:
        if rootFolder is not None and hasattr(rootFolder,"childEntity"):
            print "rootFolder hava child"
            entity_stack = rootFolder.childEntity

            while entity_stack:
                entity = entity_stack.pop()
                if isinstance(entity, vim.Datacenter):
                    # add this vim.DataCenter's folders to our search
                    # print(entity.datastoreFolder)
                    # print(entity.hostFolder)
                    # print(entity.networkFolder)
                    # print(entity.vmFolder)

                    vcDatacenterModel =  VcenterDatacenter()
                    vcDatacenterModel.name = entity.name
                    try:
                        tempDc = VcenterDatacenter.objects.filter(name=entity.name)
                        if len(tempDc)>0:
                            #如果存在则更新
                            #VcenterDatacenter.objects.filter(name='yangmv').update(pwd='520')
                            vcDatacenterModel = tempDc[0]
                        else:
                            saveVcDatacenterModel = vcDatacenterModel.save()
                            print "save dc %s" % saveVcDatacenterModel
                    except Exception as e:
                        #说明不存在
                        print "dc update  %s" % str(e)
                        vcDatacenterModel.save()

                    clusterEntityList = vmManager.get_cluster_pools(entity.hostFolder)
                    vcDatacenterModel.clusterNum = len(clusterEntityList)
                    if clusterEntityList is not None:
                        for clusterEntity in clusterEntityList:
                            vcClusterModel = VcenterCluster()
                            vcClusterModel.name = clusterEntity.name
                            vcClusterModel.datacenter = vcDatacenterModel

                            if clusterEntity.actionHistory is not None:
                                vcClusterModel.actionHistoryNum = len(clusterEntity.actionHistory)
                            else:
                                vcClusterModel.actionHistoryNum = 0

                            if clusterEntity.migrationHistory is not None:
                                vcClusterModel.migrationHistoryNum = len(clusterEntity.migrationHistory)
                            else:
                                vcClusterModel.migrationHistoryNum = 0

                            if clusterEntity.drsRecommendation is not None:
                                vcClusterModel.drsRecommendationNum = len(clusterEntity.drsRecommendation)
                            else:
                                vcClusterModel.drsRecommendationNum = 0

                            vcClusterModel.enabledClusterHa =   clusterEntity.configuration.dasConfig.enabled

                            try:
                                tempCluster =  VcenterCluster.objects.filter(name=clusterEntity.name)
                                if len(tempCluster)>0:
                                    #如果存在则更新
                                    pass
                                else:
                                    vcClusterModel.save()
                            except Exception as e:
                                #说明不存在
                                print "cluster update  %s" % str(e)
                                vcClusterModel.save()

                    datastoreEntityList = vmManager.get_datastores(entity.datastoreFolder)
                    vcDatacenterModel.datastoreNum = len(datastoreEntityList)
                    datastoreTotal = 0
                    if datastoreEntityList is not None:
                        for datastoreEntity in datastoreEntityList:

                            vcDatastoreModel = VcenterDatastore()
                            vcDatastoreModel.name = datastoreEntity.summary.name
                            vcDatastoreModel.datacenter = vcDatacenterModel
                            vcDatastoreModel.mountHostNum = len(datastoreEntity.host)

                            print "container %s "% datastoreEntity.info.containerId
                            vcDatastoreModel.datastoreContainerId = datastoreEntity.info.containerId
                            vcDatastoreModel.accessible  = datastoreEntity.summary.accessible

                            tmpCapacity = datastoreEntity.summary.capacity
                            if tmpCapacity is not None:
                                vcDatastoreModel.capacity = datastoreEntity.summary.capacity/(1024*1024)
                            else:
                                vcDatastoreModel.capacity = 0

                            tmpFreeSpace = datastoreEntity.summary.freeSpace
                            if tmpFreeSpace is not None:
                                vcDatastoreModel.freeSpace = datastoreEntity.summary.freeSpace/(1024*1024)
                            else:
                                vcDatastoreModel.freeSpace = 0
                            vcDatastoreModel.maintenanceMode = datastoreEntity.summary.maintenanceMode
                            vcDatastoreModel.multipleHostAccess = datastoreEntity.summary.multipleHostAccess
                            vcDatastoreModel.filesystemType = datastoreEntity.summary.type
                            vcDatastoreModel.url = datastoreEntity.summary.url
                            datastoreTotal+= vcDatastoreModel.capacity
                            try:
                                tempStore =  VcenterDatastore.objects.filter(name=datastoreEntity.name)
                                if len(tempStore)>0:
                                    #如果存在则更新
                                    pass
                                else:
                                    vcDatastoreModel.save()
                            except Exception as e:
                                #说明不存在
                                print "datastore update  %s" % str(e)
                                vcDatastoreModel.save()

                    vmEntityList = vmManager.get_vms(entity.vmFolder)
                    vcDatacenterModel.vmNum = len(vmEntityList)
                    if vmEntityList is not None:
                        for vmEntity in vmEntityList:
                            vcenterVirtualMachineModel = convertVmEntityToVcenterVirtualMachine(vmEntity)
                            vcenterVirtualMachineModel.datacenter = vcDatacenterModel
                            vcenterVirtualMachineModel.account = accountModel
                            vcenterVirtualMachineModel.template = False
                            try:
                                tempVm = VcenterVirtualMachine.objects.filter(instance_uuid=vcenterVirtualMachineModel.instance_uuid)
                                if len(tempVm)>0:
                                    #如果存在则更新
                                    pass
                                else:
                                    vcenterVirtualMachineModel.save()
                            except Exception as e:
                                #说明不存在
                                print "vm update  %s" % str(e)
                                vcenterVirtualMachineModel.save()

                    # print entity.name
                    # print entity.datastore
                    # print entity.network
                    vcDatacenterModel.save()
                elif hasattr(entity, 'childEntity'):
                    # add all child entities from this object to our search
                    # 子节点必须是数据中心
                    entity_stack.extend(entity.childEntity)

        res = {
            'result': True,
            'message': "同步成功",
        }
    except Exception as e:
        traceback.print_exc()
        print "root update  %s" % str(e)
        res = {
            'result': True,
            'message': "同步失败",
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

def getVcenterDatacenterList(request):
    logger.info("查询配置vcenter 数据中心")

    datacenterObjectList = VcenterDatacenter.objects.all()
    datacenterJsonList = []
    from django.forms.models import model_to_dict
    for datacenter in datacenterObjectList:
        tempDc = model_to_dict(datacenter)
        datacenterJsonList.append(tempDc)

    res = {
        "recordsTotal": len(datacenterObjectList),
        'data': datacenterJsonList
    }
    print datacenterJsonList

    return render_json(res)

def getVcenterClusterList(request):
    logger.info("查询配置vcenter 集群")

    clusterObjectList = VcenterCluster.objects.all()
    clusterJsonList = []
    from django.forms.models import model_to_dict
    for cluster in clusterObjectList:
        tempCluster = model_to_dict(cluster)
        clusterJsonList.append(tempCluster)

    res = {
        "recordsTotal": len(clusterObjectList),
        'data': clusterJsonList
    }
    return render_json(res)

def getVcenterDatastoreList(request):
    logger.info("查询配置vcenter 存储")

    datastoreObjectList = VcenterDatastore.objects.all()
    datastoreJsonList = []
    from django.forms.models import model_to_dict
    for store in datastoreObjectList:
        tempStore = model_to_dict(store)
        datastoreJsonList.append(tempStore)

    res = {
        "recordsTotal": len(datastoreObjectList),
        'data': datastoreJsonList
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

        if accountModel is None:
            res = {
                'result': True,
                'message': u"关机失败，资源账号错误",
            }
            return render_json(res)
        else:
            vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
            task = vmManager.stop(vcenterVirtualMachineModel.name)
            result = vmManager.handleTask(task)

            #同步信息
            if result == False:
                res = {
                    'result': True,
                    'message': u"关机失败",
                }
            else:
                vm = vmManager.find_by_uuid(vcenterVirtualMachineModel.instance_uuid)
                vcenterVirtualMachineModel.power_state = vm.summary.runtime.powerState
                vcenterVirtualMachineModel.save()
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

#查询状态
def queryTaskRequest(request):
    #查询状态
    pass

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

            task = vmManager.start(vcenterVirtualMachineModel.name)
            result = vmManager.handleTask(task)

            #同步信息
            if result == False:
                res = {
                    'result': True,
                    'message': u"开机失败",
                }
            else:
                vm = vmManager.find_by_uuid(vcenterVirtualMachineModel.instance_uuid)
                vcenterVirtualMachineModel.power_state = vm.summary.runtime.powerState
                vcenterVirtualMachineModel.save()
                res = {
                    'result': True,
                    'message': u"开机成功",
                }
    except Exception as e:
        traceback.print_exc()
        print str(e)
        res = {
            'result': False,
            'message': "开机失败"
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

            task = vmManager.reboot(vcenterVirtualMachineModel.name)
            result = vmManager.handleTask(task)

            #同步信息
            if result == False:
                res = {
                    'result': True,
                    'message': u"重启失败",
                }
            else:
                vm = vmManager.find_by_uuid(vcenterVirtualMachineModel.instance_uuid)
                vcenterVirtualMachineModel.power_state = vm.summary.runtime.powerState
                vcenterVirtualMachineModel.save()
                res = {
                    'result': True,
                    'message': u"重启成功",
                }

    except Exception as e:
        traceback.print_exc()
        print str(e)
        res = {
            'result': False,
            'message': u"重启成功",
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

            task = vmManager.destroy(vcenterVirtualMachineModel.name)
            result = vmManager.handleTask(task)
            #同步信息
            if result == False:
                res = {
                    'result': True,
                    'message': u"销毁失败",
                }
            else:
                # vm = vmManager.find_by_uuid(vcenterVirtualMachineModel.instance_uuid)
                # vcenterVirtualMachineModel.power_state = vm.summary.runtime.powerState
                vcenterVirtualMachineModel.delete()
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

            #同步信息
            if result == False:
                res = {
                    'result': True,
                    'message': u"克隆失败",
                }
            else:
                # vm = vmManager.find_by_uuid(vcenterVirtualMachineModel.instance_uuid)
                # vcenterVirtualMachineModel.power_state = vm.summary.runtime.powerState
                vm = vmManager.get_vm_by_name(vmName)
                cloneVmModel = convertVmEntityToVcenterVirtualMachine(vm)
                #数据中心，需要通过名字查询 todo
                cloneVmModel.datacenter = vcenterVirtualMachineModel.datacenter
                #集群需要通过名字查询 todo
                cloneVmModel.cluster = vcenterVirtualMachineModel.cluster
                cloneVmModel.account = vcenterVirtualMachineModel.account
                cloneVmModel.save()
                res = {
                    'result': True,
                    'message': u"克隆成功",
                }
    except Exception as e:
        traceback.print_exc()
        print str(e)
        res = {
            'result': False,
            'message': u"克隆失败",
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
    if allDatacenter is not None:
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
    if allDatastore is not None:
        for datastore in allDatastore:
            datastoreList.append({'id':datastore.name,'text':datastore.name})

        results['results']=datastoreList
    else:
        results['results']=datastoreList
    return render_json(results)


#获取流量分析数据
def getFlowAnalysisRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    clusters = vmManager.get_cluster_pools()

    storageList = []
    memroyList = []
    cpuList = []
    cpuCoresList = []
    analysis_data = {
        'storage':[],
        'memroy':[],
        'cpu':[],
        'cpuCores':[]
    }

    for cluster in clusters:
        datastores = cluster.datastore
        clusterForDatastoreTotal = 0
        if len(datastores) >0:
            for store in datastores:
                clusterForDatastoreTotal+=store.summary.capacity
                # print (store.summary.capacity/(1024*1024*1024*1024))
                # print (store.summary.freeSpace/(1024*1024*1024*1024))

        memroyList.append({'category':cluster.name,'value':cluster.summary.totalMemory})
        cpuList.append({'category':cluster.name,'value':cluster.summary.totalCpu})
        storageList.append({'category':cluster.name,'value':clusterForDatastoreTotal/1000})
        cpuCoresList.append({'category':cluster.name,'value':cluster.summary.numCpuCores})
    analysis_data['storage'] = storageList
    analysis_data['memroy'] = memroyList
    analysis_data['cpu'] = cpuList
    analysis_data['cpuCores'] = cpuCoresList
    print analysis_data
    return render_json(analysis_data)


#获取内存分析数据
def getMemoryAnalysisRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)

    return render_json({})

#获取CPU分析数据
def getCpuAnalysisRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    return render_json({})

#获取存储分析数据
def getStorageAnalysisRequest(request):
    accountModelList = VcenterAccount.objects.all()
    accountModel = accountModelList[0]

    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    return render_json({})







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
