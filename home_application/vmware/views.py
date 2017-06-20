# -*- coding: utf-8 -*-
import simplejson as simplejson
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

from blueking.component.base import logger
from common.mymako import render_mako_context, render_json
from home_application.models import VcenterAccount


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

def getVcenterAccountList(request):
    logger.info("getVcenterAccountList....")
    print 'getVcenterAccountList.....'
    accountObjectList = VcenterAccount.objects.all()
    accountJsonList = []
    from django.forms.models import model_to_dict
    for account in accountObjectList:
        tempAccount = model_to_dict(account)
        print tempAccount
        accountJsonList.append(tempAccount)


    print accountJsonList
    res = {
        "recordsTotal": len(accountObjectList),
        'data': accountJsonList
    }

    return render_json(res)

def createVmRequest(reqeust):
    pass

def poweroffVmRequest(reqeust):
    pass

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