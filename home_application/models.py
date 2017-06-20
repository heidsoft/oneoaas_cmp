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
