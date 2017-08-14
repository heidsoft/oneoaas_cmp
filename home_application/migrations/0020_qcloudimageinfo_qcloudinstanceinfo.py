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
                ('instance_id', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8bid')),
                ('instance_name', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u540d\u79f0')),
                ('instance_type', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u7c7b\u578b')),
                ('cpu', models.CharField(max_length=50, verbose_name='cpu')),
                ('memory', models.CharField(max_length=50, verbose_name='\u5185\u5b58')),
                ('status', models.CharField(max_length=50, verbose_name='\u5b9e\u4f8b\u72b6\u6001')),
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
    ]
