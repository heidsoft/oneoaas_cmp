# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0008_remove_vcentervirtualmachine_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='boot_time',
            field=models.TimeField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='instance_uuid',
            field=models.CharField(default=datetime.datetime(2017, 6, 22, 15, 34, 40, 825255), max_length=40),
            preserve_default=False,
        ),
    ]
