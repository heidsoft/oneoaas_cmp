# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from common.mymako import render_mako_context
from home_application.models import VcenterAccount
from hybirdsdk.virtualMachine import VmManage


def home(request):
    """主首页"""
    import settings
    return HttpResponseRedirect(settings.SITE_URL+"overview/")

def overview(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    data={
        'datacenter':None,
        'cluster':None,
        'vm':None,
        'storage':None
    }

    try:
        accountModelList = VcenterAccount.objects.all()
        accountModel = accountModelList[0]
    except Exception as e:
       print("Caught exception : " + str(e))
       data['vm'] = "Unkonw"
       data['cluster'] = "Unkonw"
       data['datacenter'] = "Unkonw"
       data['storage'] = "Unkonw"
       return render_mako_context(
           request, '/home_application/overview/overview.html',data
       )

    data={
        'datacenter':None,
        'cluster':None,
        'vm':None,
        'storage':None
    }
    vmManager = VmManage(host=accountModel.vcenter_host,user=accountModel.account_name,password=accountModel.account_password,port=accountModel.vcenter_port,ssl=None)
    vms = vmManager.get_vms()
    datacenters = vmManager.get_datacenters()
    clusters = vmManager.get_resource_pools()
    datastores = vmManager.get_datastores_info()


    datastores_all_capacity = datastores['datastores_all_capacity']
    if datastores_all_capacity is not None and datastores_all_capacity > 0:
        data['storage'] = datastores_all_capacity/(1024*1024*1024*1024)
    else:
        data['storage'] = "Unkonw"

    data['vm'] = len(vms)
    data['cluster'] = len(clusters)
    data['datacenter'] = len(datacenters)


    return render_mako_context(
        request, '/home_application/overview/overview.html',data
    )


