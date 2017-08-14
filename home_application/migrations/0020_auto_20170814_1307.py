# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0019_auto_20170809_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='QcloudImageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_id', models.CharField(max_length=50, verbose_name='\u955c\u50cfid')),
                ('osname', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u540d\u79f0')),
                ('image_size', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u5bb9\u91cf\uff08GiB\uff09')),
                ('image_type', models.IntegerField(verbose_name='\u955c\u50cf\u7c7b\u578b')),
                ('created_time', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u521b\u5efa\u65f6\u95f4')),
                ('image_state', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u72b6\u6001')),
                ('image_source', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u6765\u6e90')),
                ('image_name', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u540d\u79f0')),
                ('image_description', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u8be6\u7ec6\u63cf\u8ff0')),
                ('image_creator', models.CharField(max_length=50, verbose_name='\u955c\u50cf\u521b\u5efa\u8005')),
                ('operation_mask', models.CharField(max_length=50, verbose_name='')),
            ],
            options={
                'db_table': 'qcloud_image_info',
            },
        ),
        migrations.CreateModel(
            name='QcloudInstanceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_id', models.CharField(unique=True, max_length=50, verbose_name='\u5b9e\u4f8bid')),
                ('instance_name', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u540d\u79f0')),
                ('instance_type', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u7c7b\u578b')),
                ('cpu', models.IntegerField(verbose_name='cpu')),
                ('memory', models.IntegerField(verbose_name='\u5185\u5b58')),
                ('status', models.CharField(default=b'RUNNING', max_length=50, verbose_name='\u5b9e\u4f8b\u72b6\u6001(PENDING\u51c6\u5907\u4e2d,RUNNING\u8fd0\u884c\u4e2d,STOPPED\u5df2\u505c\u6b62,REBOOTING\u91cd\u542f\u4e2d,STARTING\u542f\u52a8\u4e2d,STOPPING\u505c\u6b62\u4e2d,EXPIRED\u5df2\u8fc7\u671f,TERMINATING\u9000\u8fd8\u4e2d,TERMINATED\u5df2\u9000\u8fd8)')),
                ('zone', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u6240\u5c5e\u5730\u57df')),
                ('instance_charge_type', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u8ba1\u8d39\u6a21\u5f0f')),
                ('private_ip_addresses', models.CharField(max_length=50, verbose_name='\u5185\u7f51ip')),
                ('public_ip_addresses', models.CharField(max_length=50, verbose_name='\u5916\u7f51ip')),
                ('image_id', models.CharField(max_length=50, verbose_name='\u955c\u50cfid')),
                ('os_name', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u540d\u79f0')),
                ('system_disk_type', models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u76d8\u7c7b\u578b')),
                ('system_disk_size', models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u76d8\u5c3a\u5bf8')),
                ('renew_flag', models.CharField(max_length=50, verbose_name='\u81ea\u52a8\u7eed\u8d39\u6807\u8bc6')),
                ('internet_max_bandwidth_out', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u7f51\u7edc\u5e26\u5bbd\u4e0a\u9650')),
                ('internet_charge_type', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u7f51\u7edc\u8ba1\u8d39\u7c7b\u578b')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5b9e\u4f8b\u521b\u5efa\u65f6\u95f4')),
                ('expired_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5b9e\u4f8b\u5230\u671f\u65f6\u95f4')),
            ],
            options={
                'db_table': 'qcloud_instance_info',
            },
        ),
        migrations.CreateModel(
            name='UcloudInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autoRenew', models.CharField(default=b'', max_length=5, null=True)),
                ('basicImageId', models.CharField(default=b'', max_length=15, null=True)),
                ('basicImageName', models.CharField(default=b'', max_length=30, null=True)),
                ('bootDiskState', models.CharField(default=b'', max_length=10, null=True)),
                ('cpu', models.IntegerField(default=0, null=True)),
                ('chargeType', models.CharField(default=b'', max_length=15, null=True)),
                ('createTime', models.TimeField(null=True)),
                ('backupType', models.CharField(default=b'', max_length=15, null=True)),
                ('diskId', models.CharField(default=b'', max_length=15, null=True, verbose_name='\u78c1\u76d8id')),
                ('drive', models.CharField(default=b'', max_length=15, null=True, verbose_name='\u78c1\u76d8\u9a71\u52a8')),
                ('encrypted', models.CharField(default=b'No', max_length=5, null=True, verbose_name='\u78c1\u76d8\u662f\u5426\u52a0\u5bc6')),
                ('size', models.IntegerField(default=0, null=True, verbose_name='\u78c1\u76d8\u5927\u5c0f')),
                ('type', models.CharField(default=b'Boot', max_length=10, null=True, verbose_name='\u78c1\u76d8\u7c7b\u578b')),
                ('expireTime', models.TimeField(null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('gpu', models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u5f00\u542fGPU')),
                ('hostType', models.CharField(default=b'', max_length=10, null=True, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('hotplugFeature', models.BooleanField(default=False, max_length=10, verbose_name='\u662f\u5426\u70ed\u63d2\u62d4\u7279\u6027')),
                ('privateSubnetId', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u79c1\u6709\u5b50\u7f51id')),
                ('privateIP', models.CharField(default=b'', max_length=20, null=True, verbose_name='')),
                ('privateVPCId', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u5b50\u7f51VPCid')),
                ('publicBandwidth', models.IntegerField(default=0, null=True, verbose_name='\u516c\u5171\u5e26\u5bbd')),
                ('publicIP', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u516c\u5171IP')),
                ('publicIPId', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u516c\u5171IPid')),
                ('publicType', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u516c\u5171IP\u7c7b\u578b')),
                ('publicWeight', models.IntegerField(default=0, null=True, verbose_name='\u6743\u91cd')),
                ('imageId', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u955c\u50cfID')),
                ('isExpire', models.CharField(default=b'No', max_length=5, null=True, verbose_name='\u662f\u5426\u8fc7\u671f')),
                ('memory', models.IntegerField(default=0, null=True, verbose_name='\u5185\u5b58')),
                ('name', models.CharField(default=b'', max_length=40, verbose_name='\u540d\u79f0')),
                ('netCapFeature', models.BooleanField(default=False)),
                ('netCapability', models.CharField(default=b'Normal', max_length=20, null=True)),
                ('networkState', models.CharField(default=b'NotConnected', max_length=20, null=True)),
                ('osName', models.CharField(default=b'', max_length=30, null=True)),
                ('osType', models.CharField(default=b'', max_length=10, null=True)),
                ('remark', models.CharField(default=b'', max_length=100, null=True)),
                ('state', models.CharField(default=b'', max_length=15, null=True)),
                ('storageType', models.CharField(default=b'', max_length=15, null=True)),
                ('subnetType', models.CharField(default=b'', max_length=15, null=True)),
                ('tag', models.CharField(default=b'', max_length=15, null=True)),
                ('timemachineFeature', models.CharField(default=b'', max_length=5, null=True)),
                ('totalDiskSpace', models.IntegerField(default=0, null=True)),
                ('uHostId', models.CharField(default=b'', max_length=15, null=True)),
                ('uHostType', models.CharField(default=b'', max_length=15, null=True)),
                ('zone', models.CharField(default=b'', max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='account_password',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
    ]
