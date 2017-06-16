# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.vmware.views',
    url(r'^manage/$', 'getVmManageView'),
    url(r'^config/$', 'getVmConfigView'),
    url(r'^api/getVcenterAccountList/$', 'getVcenterAccountList'),
)