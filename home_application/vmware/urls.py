# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.vmware.views',
    url(r'^vm/manage', 'getVmManageView'),
    url(r'^cluster/manage', 'getClusterManageView'),
    url(r'^datacenter/manage', 'getDatacenterManageView'),
    url(r'^department/manage', 'getDepartmentManageView'),
    url(r'^department/resource/manage', 'getDepartmentResourceManageView'),
    url(r'^user/manage', 'getUserManageView'),
    url(r'^storage/manage', 'getStorageManageView'),

    url(r'^monitor/config/$', 'getMonitorConfigView'),
    url(r'^system/config/$', 'getVmConfigView'),

    url(r'api/getVcenterAccountList$', 'getVcenterAccountList'),
    url(r'api/createVCenterAccount$', 'createVCenterAccount'),
    url(r'api/syncVCenterAccount', 'syncVCenterAccount'),
    url(r'api/getVcenterVirtualMachineList', 'getVcenterVirtualMachineList'),
    url(r'api/poweroff', 'poweroffVmRequest'),
    url(r'api/start', 'startVmRequest'),
    url(r'api/reboot', 'rebootVmRequest'),
    url(r'api/destroy', 'destroyVmRequest'),
    url(r'api/getAppList', 'getAppList'),
    url(r'api/async', 'asyncDemo'),



)
