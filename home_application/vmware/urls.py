# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.vmware.views',
    url(r'^manage', 'getVmManageView'),
    url(r'^config/$', 'getVmConfigView'),
    url(r'api/getVcenterAccountList$', 'getVcenterAccountList'),
    url(r'api/createVCenterAccount$', 'createVCenterAccount'),
    url(r'api/syncVCenterAccount', 'syncVCenterAccount'),
    url(r'api/getVcenterVirtualMachineList', 'getVcenterVirtualMachineList'),
    url(r'api/poweroff', 'poweroffVmRequest'),
    url(r'api/start', 'startVmRequest'),
    url(r'api/reboot', 'rebootVmRequest'),
    url(r'api/destroy', 'destroyVmRequest'),

)