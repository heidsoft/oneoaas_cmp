# -*- coding: utf-8 -*-
import json
from django.db import models

"""
vcenter账号信息对象
"""
class VcenterAccount(models.Model):
    account_name = models.CharField(max_length=60)
    account_password = models.IntegerField(null=40)
    vcenter_host = models.CharField(max_length=40)
    vcenter_version = models.CharField(max_length=60)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_account'
