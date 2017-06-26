# -*- coding: utf-8 -*-
import simplejson as simplejson
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

from blueking.component.base import logger
from common.mymako import render_mako_context, render_json
from home_application.models import VcenterAccount, VcenterVirtualMachine
from hybirdsdk.virtualMachine import VmManage,vmware_client
from pyVmomi import vim, vmodl

def getVmManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_manage.html'
    )


def getVmConfigView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_config.html'
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
"""
同步账号
"""
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
                vmTempModel.save()

        res = {
            'result': True,
            'message': "同步成功",
        }

    return render_json(res)

"""
查询vcenter账号配置
"""
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

def getVcenterVirtualMachineList(request):
    logger.info("查询配置vcenter 虚拟机")

    vcenterVirtualMachineObjectList = VcenterVirtualMachine.objects.all()
    vmJsonList = []
    from django.forms.models import model_to_dict
    for vm in vcenterVirtualMachineObjectList:
        tempvm = model_to_dict(vm)
        vmJsonList.append(tempvm)

    res = {
        "recordsTotal": len(vmJsonList),
        'data': vmJsonList
    }

    return render_json(res)

def createVmRequest(request):
    pass

def poweroffVmRequest(request):

    try:
        if request.method == 'POST':
            vmId = request.POST['vmId']
            accountId = request.POST['accountId']

            vcenterVirtualMachineModel = VcenterVirtualMachine.objects.get(id=vmId)
            accountModel = VcenterAccount.objects.get(id=accountId)


        vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
        vmAllList = vmManager.list()

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

def startVmRequest(reqeust):
    pass

def rebootVmRequest(reqeust):
    pass

def destroyVmRequest(reqeust):
    pass

def cloneVmRequest(reqeust):
    pass

def WebSSHVmRequest(reqeust):
    pass