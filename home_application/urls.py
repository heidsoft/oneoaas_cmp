# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',
    # 首页
    url(r'^$', "home_application.overview.views.home"),
    url(r'^overview/', include('home_application.overview.urls')),
    url(r'^qcloud/', include('home_application.qcloud.urls')),
    url(r'^vmware/', include('home_application.vmware.urls')),
    url(r'^ucloud/', include('home_application.ucloud.urls')),
    url(r'^aws/', include('home_application.aws.urls')),
    url(r'^aliyun/', include('home_application.aliyun.urls')),
    url(r'^event/', include('home_application.event.urls')),
    # (r'^dashboard$','dashboard'),
    # (r'^hello$','hello'),

    # (r'^view/(.+)/$', 'view'),
    # (r'^queryHost', 'queryHost'),
    # (r'^grid$', 'grid'),
    # (r'^forms$', 'forms'),
    # (r'^dev-guide/$', 'dev_guide'),
    # (r'^contactus/$', 'contactus'),
    # (r'^useradd', 'useradd'),
    # (r'^userlist', 'userlist'),
    # (r'^execute/task$', 'executeTask'),
    # (r'^execute/job$', 'executeJob'),
    # (r'^hosts$', 'getHosts'),
    # (r'^jobs', 'getJobs'),
)

