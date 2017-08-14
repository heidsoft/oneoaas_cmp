# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0023_auto_20170813_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcloudinstanceinfo',
            name='instance_id',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u5b9e\u4f8bid'),
        ),
    ]
