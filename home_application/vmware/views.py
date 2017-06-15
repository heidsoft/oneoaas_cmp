# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from common.mymako import render_mako_context


def getVmManageView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_manage.html'
    )


def getVmConfigView(request):
    return render_mako_context(
        request, '/home_application/vmware/vmware_config.html'
    )


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