# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from common.log import logger
from common.mymako import render_mako_context, render_json
from home_application.models import VcenterAccount, UcloudInstance
from hybirdsdk.ucloud.sdk import UcloudApiClient
from hybirdsdk.ucloud.config import base_url


def ucloud(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/ucloud/ucloud.html'
    )


def syncUcloudAccount(request):
    accountId = None
    if request.method == 'POST':
        accountId = request.POST['id']
        logger.info( "accountId is %s" % accountId)
        if accountId is None or accountId < 0:
            res = {
                'result': True,
                'message': "该账号不存在",
            }
            return render_json(res)

        accountModel = VcenterAccount.objects.get(id=accountId)
        public_key = accountModel.cloud_public_key
        private_key = accountModel.cloud_private_key
        ApiClient = UcloudApiClient(base_url, public_key, private_key)
        Parameters={
            "Action":"DescribeUHostInstance",
            "Region":"cn-sh2",
        }
        response = ApiClient.get("/", Parameters)
        print response

#获取ucloud虚拟机列表
def getUcloudInstanceList(request):
    logger.info("查询配置vcenter 虚拟机")
    instanceList = UcloudInstance.objects.all()
    print instanceList
    vmJsonList = []
    from django.forms.models import model_to_dict
    for vm in instanceList:
        tempvm = model_to_dict(vm)
        vmJsonList.append(tempvm)
    res = {
        "recordsTotal": len(vmJsonList),
        'data': vmJsonList
    }
    return render_json(res)