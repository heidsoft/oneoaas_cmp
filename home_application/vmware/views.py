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


