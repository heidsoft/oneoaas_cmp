# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from blueking.component.base import logger
from common.mymako import render_mako_context, render_json


def getVmManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_manage.html'
    )


def getVmConfigView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_config.html'
    )


def getVcenterAccountList(request):
    logger.info("getVcenterAccountList....")
    print 'getVcenterAccountList.....'
    res = {
        "draw": 2,
        "recordsTotal": 21,
        "recordsFiltered": 5,
        'data': [
            {"test1":1111,"test2":444,"test3":3333},
            {"test1":1111,"test2":55,"test3":3333},
            {"test1":1111,"test2":99,"test3":3333},
            {"test1":1111,"test2":66,"test3":3333},
            {"test1":1111,"test2":2222,"test3":3333},
            {"test1":1111,"test2":664,"test3":3333},
            {"test1":1111,"test2":88,"test3":3333},
            {"test1":1111,"test2":444,"test3":3333},
            {"test1":1111,"test2":55,"test3":3333},
            {"test1":1111,"test2":99,"test3":3333},
            {"test1":1111,"test2":66,"test3":3333},
            {"test1":1111,"test2":2222,"test3":3333},
            {"test1":1111,"test2":664,"test3":3333},
            {"test1":1111,"test2":88,"test3":3333},
            {"test1":1111,"test2":444,"test3":3333},
            {"test1":1111,"test2":55,"test3":3333},
            {"test1":1111,"test2":99,"test3":3333},
            {"test1":1111,"test2":66,"test3":3333},
            {"test1":1111,"test2":2222,"test3":3333},
            {"test1":1111,"test2":664,"test3":3333},
            {"test1":1111,"test2":88,"test3":3333}
        ]
    }
    print res
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