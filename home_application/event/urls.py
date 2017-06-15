# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.event.views',
    url(r'^type/$', 'type'),
    url(r'^manage/$', 'manage'),
    url(r'^workflow/$', 'workflow'),
    url(r'^alarmcompression/$', 'alarmCompression'),
    url(r'^alarmmerge/$', 'alarmMerge'),
    url(r'^eventTypeAdd/$', 'eventTypeAdd'),
    url(r'^eventConfig/$', 'eventConfig'),
    url(r'^eventUserManage/$', 'eventUserManage'),
    url(r'^addEventSource/$', 'addEventSource'),


)
