# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from common.mymako import render_mako_context

def home(request):
    """主首页"""
    import settings
    return HttpResponseRedirect(
        settings.SITE_URL+"overview/")

def overview(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。

    return render_mako_context(
        request, '/home_application/overview/overview.html'
    )


