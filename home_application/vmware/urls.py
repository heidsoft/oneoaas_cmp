# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.vmware.views',
    url(r'^$', 'vmware'),
)