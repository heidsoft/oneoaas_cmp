# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0022_auto_20170813_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcloudinstanceinfo',
            name='status',
            field=models.CharField(default=b'RUNNING', max_length=50, verbose_name='\u5b9e\u4f8b\u72b6\u6001(PENDING\u51c6\u5907\u4e2d,RUNNING\u8fd0\u884c\u4e2d,STOPPED\u5df2\u505c\u6b62,REBOOTING\u91cd\u542f\u4e2d,STARTING\u542f\u52a8\u4e2d,STOPPING\u505c\u6b62\u4e2d,EXPIRED\u5df2\u8fc7\u671f,TERMINATING\u9000\u8fd8\u4e2d,TERMINATED\u5df2\u9000\u8fd8)'),
        ),
    ]
