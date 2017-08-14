# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect

from common.mymako import render_mako_context
from QcloudApi.qcloudapi import QcloudApi
import traceback
from common.mymako import render_mako_context, render_json
from home_application.models import *
import utils
import json
import time
import pytz
import datetime
import math

# AKIDuzyiMrVHE4uo7QQVM7i8XsmVs585nTtC
# MXlPuIUVM51rZ9aqz87ukPuENK6kHetA
def qcloud(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/qcloud/qcloud.html'
    )


'''
查询腾讯云的账号信息
'''
def getQcloudAccountList(request):
    accountObjectList = VcenterAccount.objects.filter(cloud_provider='qcloud')
    accountJsonList = []
    from django.forms.models import model_to_dict
    for account in accountObjectList:
        tempAccount = model_to_dict(account)
        accountJsonList.append(tempAccount)
    res = {
        "recordsTotal": len(accountObjectList),
        'data': accountJsonList
    }
    return render_json(res)



'''
同步腾讯云的虚拟机实例信息
'''
def syncDescribeInstances(request):
    accountObjectList = VcenterAccount.objects.filter(cloud_provider='qcloud')
    if accountObjectList is None or len(accountObjectList) <= 0:
        pass
    else:
        qcloudAccount = accountObjectList[0]
        account_name = str(qcloudAccount.account_name)
        account_password = str(qcloudAccount.account_password)
        version = str(qcloudAccount.vcenter_version)
        print 'account_name : %s' % account_name
        print 'account_password : %s' % account_password
        print 'version : %s' % version
        module = 'cvm'
        '''
        action 对应接口的接口名，请参考产品文档上对应接口的接口名
        '''
        action = 'DescribeInstances'
        Offset = 0
        Limit = 100
        params = {}
        result = utils.getInstances(module, action, account_name, account_password, version, Offset, Limit)
        result = json.loads(result)
        if 'Response' in result and result.get('Response') is not None:
            myResponse = result.get('Response')
            # 说明请求成功，可以正常获得结果集
            totalCount = myResponse.get('TotalCount')
            instanceSet = myResponse.get('InstanceSet')
            # print 'totalCount :%s'% totalCount
            # 单次可以取完所有数据
            instanceList = []
            params['Version'] = version
            params['Offset'] = Offset
            params['Limit'] = Limit
            if totalCount is not None and totalCount <= 100:
                for i in range(len(instanceSet)):
                    myinstance = instanceSet[i]
                    instanceId = str(myinstance.get('InstanceId'))
                    instanceName = str(myinstance.get('InstanceName'))
                    instanceType = str(myinstance.get('InstanceType'))
                    cpu = int(myinstance.get('CPU'))
                    memory = int(myinstance.get('Memory'))
                    status = 'RUNNING'
                    instanceChargeType = str(myinstance.get('InstanceChargeType'))
                    zone = str(myinstance.get('Placement').get('Zone'))
                    privateIp = str(myinstance.get('PrivateIpAddresses')[0])
                    publicIp = str(myinstance.get('PublicIpAddresses')[0])
                    imageId = str(myinstance.get('ImageId'))
                    osName = str(myinstance.get('OsName'))
                    systemDiskType = str(myinstance.get('SystemDisk').get('DiskType'))
                    systemDiskSize = int(myinstance.get('SystemDisk').get('DiskSize'))
                    internetMaxBandwidthOut = int(myinstance.get('InternetAccessible').get('InternetMaxBandwidthOut'))
                    internetChargeType = str(myinstance.get('InternetAccessible').get('InternetChargeType'))
                    renewFlag = str(myinstance.get('RenewFlag'))
                    createdTime = myinstance.get('CreatedTime')
                    expiredTime = myinstance.get('ExpiredTime')
                    createdTime = utils.utc_to_local(createdTime)
                    expiredTime = utils.utc_to_local(expiredTime)
                    instance = QcloudInstanceInfo()
                    instance.instance_id = instanceId
                    instance.instance_name = instanceName
                    instance.instance_type = instanceType
                    instance.instance_charge_type = instanceChargeType
                    instance.cpu = cpu
                    instance.memory = memory
                    instance.status = status
                    instance.zone = zone
                    instance.private_ip_addresses = privateIp
                    instance.public_ip_addresses = publicIp
                    instance.image_id = imageId
                    instance.os_name = osName
                    instance.system_disk_size = systemDiskSize
                    instance.system_disk_type = systemDiskType
                    instance.internet_charge_type = internetChargeType
                    instance.internet_max_bandwidth_out = internetMaxBandwidthOut
                    instance.renew_flag = renewFlag
                    instance.created_time = createdTime
                    instance.expired_time = expiredTime
                    instanceList.append(instance)
                    key = 'InstanceIds.' + str(i + 1)
                    params[key] = instanceId
                statusrs = utils.requestQcloud(module, 'DescribeInstancesStatus', account_name, account_password, params)
                statusrs = json.loads(statusrs)
                if 'Response' in statusrs and statusrs.get('Response') is not None:
                    statusResponse = statusrs.get('Response')
                    # 说明请求成功，可以正常获得结果集
                    statustotalCount = statusResponse.get('TotalCount')
                    InstanceStatusSet = statusResponse.get('InstanceStatusSet')
                    statusdict = {}
                    if totalCount == statustotalCount:
                        for m in range(len(InstanceStatusSet)):
                            instanceStatus = InstanceStatusSet[m]
                            instanceId = instanceStatus.get('InstanceId')
                            instanceState = instanceStatus.get('InstanceState')
                            statusdict[instanceId] = instanceState
                        for j in range(len(instanceList)):
                            getinstance = instanceList[j]
                            finalstatus = statusdict.get(getinstance.instance_id)
                            getinstance.status = finalstatus
                    else:
                        # 如果实例状态的数量与实例数量不一致，说明有些实例没有正常取到状态
                        pass
                QcloudInstanceInfo.objects.bulk_create(instanceList)
                responseResult = {
                    'result': True,
                    "content": {},
                    "message": u"操作成功"
                }
                return render_json(responseResult)
            else:
                num = int(math.ceil(float(totalCount) / Limit))
                for i in range(num, -1, -1):
                    pass
        else:
            pass



'''
同步镜像信息
'''
def syncImages(request):
    pass



'''
查询腾讯云虚拟机实例列表
'''
def getQcloudVmList(request):
    module = 'cvm'

    '''
    action 对应接口的接口名，请参考产品文档上对应接口的接口名
    '''
    action = 'DescribeInstances'

    config = {
        'Region': 'ap-shanghai',
        'secretId': 'AKIDuzyiMrVHE4uo7QQVM7i8XsmVs585nTtC',
        'secretKey': 'MXlPuIUVM51rZ9aqz87ukPuENK6kHetA',
        'method': 'get'
    }

    '''
    params 请求参数，请参考产品文档上对应接口的说明
    '''
    params = {

        # 'Version':'2017-03-12'
        # 'userIp': '127.0.0.1',
        # 'businessId': 1,
        # 'captchaType': 1,
        # 'script': 0,
        # 'Region': 'gz', # 当Region不是上面配置的DefaultRegion值时，可以重新指定请求的Region
    }
    try:
        service = QcloudApi(module, config)

        # 请求前可以通过下面四个方法重新设置请求的secretId/secretKey/region/method参数
        # 重新设置请求的secretId
        # secretId = 'AKIDuzyiMrVHE4uo7QQVM7i8XsmVs585nTtC'
        # service.setSecretId(secretId)
        # # 重新设置请求的secretKey
        # secretKey = 'MXlPuIUVM51rZ9aqz87ukPuENK6kHetA'
        # service.setSecretKey(secretKey)
        # # 重新设置请求的region
        # region = 'ap-shanghai'
        # service.setRegion(region)
        # # 重新设置请求的method
        # method = 'get'
        # service.setRequestMethod(method)

        # 生成请求的URL，不发起请求
        print service.generateUrl(action, params)
        # 调用接口，发起请求
        print params
        print service.call(action, params)
    except Exception, e:
        traceback.print_exc()
        print 'exception:', e



'''
腾讯云启动虚拟机实例
'''
def startQcloudVm(request):
    vmIds = request.POST.getlist('vmIds')
    vmInstanceIds = request.POST.getlist('instanceids')
    responseResult = {
        'result': True,
        "content": {},
        "message": u"操作成功"
    }
    if vmIds is None or vmInstanceIds is None or len(vmIds) == 0 or vmInstanceIds == 0:
        # 虚拟机的信息不全无法进行操作
        res = {
            'result': False,
            'message': u"虚拟机信息不正确,无法进行开启操作",
        }
        return render_json(res)
    accountObjectList = VcenterAccount.objects.filter(cloud_provider='qcloud')
    if accountObjectList is None or len(accountObjectList) <= 0:
        # 虚拟机的信息不全无法进行操作
        res = {
            'result': False,
            'message': u"腾讯云账号有误，无法正常使用",
        }
        return render_json(res)
    else:
        qcloudAccount = accountObjectList[0]
        account_name = qcloudAccount.get('account_name')
        account_password = qcloudAccount.get('account_password')
        version = qcloudAccount.get('vcenter_version')
        module = 'cvm'
        '''
        action 对应接口的接口名，请参考产品文档上对应接口的接口名
        '''
        action = 'StartInstances'
        config = {
            'Region': 'ap-shanghai',
            'secretId': account_name,
            'secretKey': account_password,
            'method': 'get'
        }
        '''
        params 请求参数，请参考产品文档上对应接口的说明
        '''
        params = {
            'Version': version
        }
    if len(vmInstanceIds) == 1:
        params['InstanceIds.1'] =vmInstanceIds[0]
    else:
        for i in range(len(vmInstanceIds)):
            key = 'InstanceIds.'+str(i+1)
            params[key] = vmInstanceIds[i]
    try:
        service = QcloudApi(module, config)
        # 生成请求的URL，不发起请求
        service.generateUrl(action, params)
        # 调用接口，发起请求
        print params
        result = service.call(action, params)
        if 'RequestId' in result:
            return render_json(responseResult)
        else:
            res = {
                'result': False,
                'message': u"操作失败",
            }
            return render_json(res)
    except Exception, e:
        traceback.print_exc()
        print 'exception:', e



'''
腾讯云停止虚拟机实例
'''
def stopQcloudVm(request):
    vmIds = request.POST.getlist('vmIds')
    vmInstanceIds = request.POST.getlist('instanceids')
    responseResult = {
        'result': True,
        "content": {},
        "message": u"操作成功"
    }
    if vmIds is None or vmInstanceIds is None or len(vmIds) == 0 or vmInstanceIds == 0:
        # 虚拟机的信息不全无法进行操作
        res = {
            'result': False,
            'message': u"虚拟机信息不正确,无法进行开启操作",
        }
        return render_json(res)
    accountObjectList = VcenterAccount.objects.filter(cloud_provider='qcloud')
    if accountObjectList is None or len(accountObjectList) <= 0:
        # 虚拟机的信息不全无法进行操作
        res = {
            'result': False,
            'message': u"腾讯云账号有误，无法正常使用",
        }
        return render_json(res)
    else:
        qcloudAccount = accountObjectList[0]
        account_name = qcloudAccount.get('account_name')
        account_password = qcloudAccount.get('account_password')
        version = qcloudAccount.get('vcenter_version')
        module = 'cvm'
        '''
        action 对应接口的接口名，请参考产品文档上对应接口的接口名
        '''
        action = 'StopInstances'
        config = {
            'Region': 'ap-shanghai',
            'secretId': account_name,
            'secretKey': account_password,
            'method': 'get'
        }
        '''
        params 请求参数，请参考产品文档上对应接口的说明
        '''
        params = {
            'Version': version
        }
    if len(vmInstanceIds) == 1:
        params['InstanceIds.1'] = vmInstanceIds[0]
    else:
        for i in range(len(vmInstanceIds)):
            key = 'InstanceIds.' + str(i + 1)
            params[key] = vmInstanceIds[i]
    try:
        service = QcloudApi(module, config)
        # 生成请求的URL，不发起请求
        service.generateUrl(action, params)
        # 调用接口，发起请求
        print params
        result = service.call(action, params)
        if 'RequestId' in result:
            return render_json(responseResult)
        else:
            res = {
                'result': False,
                'message': u"操作失败",
            }
            return render_json(res)
    except Exception, e:
        traceback.print_exc()
        print 'exception:', e


