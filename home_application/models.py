# -*- coding: utf-8 -*-
import json

import datetime
from django.db import models

"""
vcenter账号信息对象
"""
class VcenterAccount(models.Model):
    account_name = models.CharField(max_length=60)
    account_password = models.CharField(max_length=20)
    vcenter_host = models.CharField(max_length=30)
    vcenter_port = models.IntegerField(default=443)
    vcenter_version = models.CharField(max_length=10)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_account'

        """
数据中心,与虚拟机是一对多的关系
        与集群是一对多的关系
"""
class VcenterDatacenter(models.Model):
    #数据中心名称
    name = models.CharField(max_length=60)

    #存储节点总量
    datastoreTotal = models.IntegerField(default=0)

    #存储节点个数
    datastoreNum = models.IntegerField(default=0)

    #主机个数
    hostNum = models.IntegerField(default=0)

    #网络个数
    networkNum = models.IntegerField(default=0)

    #虚拟机个数
    vmNum = models.IntegerField(default=0)

    #集群个数
    clusterNum = models.IntegerField(default=0)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_datacenter'

"""
集群，与数据中心是一对多关系
"""
class VcenterCluster(models.Model):
    #集群所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_cluster_ref_datacenter')

    #集群名称
    name = models.CharField(max_length=60)

    #集群操作历史次数
    actionHistoryNum = models.IntegerField(default=0)

    #集群迁移历史次数
    migrationHistoryNum = models.IntegerField(default=0)

    #drs推荐次数
    drsRecommendationNum = models.IntegerField(default=0)

    #集群是否开启HA
    enabledClusterHa  = models.BooleanField(default=False)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_cluster'

"""
存储节点，与数据中心是一对多关系
"""
class VcenterDatastore(models.Model):
    #存储所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_datastore_ref_datacenter')
    #存储节点名称
    name = models.CharField(max_length=60)

    #存储挂载主机数
    mountHostNum = models.IntegerField(default=0)

    #存储节点容器id
    datastoreContainerId = models.CharField(default="",max_length=60)

    #是否可访问
    accessible = models.BooleanField(default=True)

    #容量大小
    capacity = models.IntegerField(default=0)

    #剩余空间
    freeSpace = models.IntegerField(default=0)

    #维护模式
    maintenanceMode = models.CharField(default="",max_length=20)

    #多主机访问是否开启
    multipleHostAccess = models.BooleanField(default=True,max_length=20)

    #文件系统类型
    filesystemType = models.CharField(default="",max_length=20)

    #存储节点路径
    url = models.CharField(default="",max_length=120)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_datastore'

"""
存储节点，与数据中心是一对多关系
"""
class VcenterNetwork(models.Model):
    #网络所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_network_ref_datacenter')
    #数据中心名称
    name = models.CharField(max_length=60)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_network'

"""
vcenter虚拟机对象
"""
class VcenterVirtualMachine(models.Model):
    #属于哪一个vcenter 账号
    account = models.ForeignKey(VcenterAccount, related_name='vcenter_virtualmachine_ref_account')

    #虚拟机所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_virtualmachine_ref_datacenter')

    #虚拟机所在集群
    cluster = models.ForeignKey(VcenterCluster, related_name='vcenter_virtualmachine_ref_cluster')

    #虚拟机名称
    name = models.CharField(max_length=60)
    #虚拟机路径名称
    vm_pathname = models.CharField(max_length=120)
    #虚拟机操作系统名称
    guest_fullname = models.CharField(max_length=60)
    #虚拟机运行状态
    power_state = models.CharField(max_length=50)
    #虚拟机IP
    ipaddress = models.CharField(max_length=30)
    #实例uuid
    instance_uuid = models.CharField(max_length=40)
    #最后启动时间
    boot_time = models.TimeField(null=True)

    #是否为模版
    template = models.BooleanField(max_length=1)

    #最大cpu使用
    maxCpuUsage = models.IntegerField(default=0)
    #最大内存使用
    maxMemoryUsage = models.IntegerField(default=0)
    #内存大小
    memorySizeMB = models.IntegerField(default=0)
    #cpu个数
    numCpu = models.IntegerField(default=0)

    numEthernetCards = models.IntegerField(default=0)

    numVirtualDisks = models.IntegerField(default=0)

    instanceUuid = models.CharField(max_length=60)

    #操作系统Id
    guestId = models.CharField(max_length=60)

    #存储信息
    storage_committed = models.IntegerField(default=0,null=True),
    storage_uncommitted = models.IntegerField(default=0,null=True),
    storage_unshared = models.IntegerField(default=0,null=True),

    overallStatus = models.CharField(max_length=10)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_virtualmachine'


