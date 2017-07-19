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
    vcenter_port = models.IntegerField(max_length=10)
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

    #自定义表名称
    class Meta:
        db_table = 'vcenter_datacenter'

"""
集群，与数据中心是一对多关系
"""
class VcenterCluster(models.Model):
    #集群所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_cluster_ref_datacenter')
    #数据中心名称
    name = models.CharField(max_length=60)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_cluster'

"""
存储节点，与数据中心是一对多关系
"""
class VcenterDatastore(models.Model):
    #存储所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_datastore_ref_datacenter')
    #数据中心名称
    name = models.CharField(max_length=60)

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
    boot_time = models.TimeField(max_length=20,null=True)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_virtualmachine'


