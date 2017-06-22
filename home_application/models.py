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
vcenter虚拟机对象
"""
class VcenterVirtualMachine(models.Model):
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
    boot_time = models.CharField(max_length=20)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_virtualmachine'
