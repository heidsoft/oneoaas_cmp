# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20170719_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenteraccount',
            name='vcenter_port',
            field=models.IntegerField(default=443),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='boot_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='maxCpuUsage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='maxMemoryUsage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='memorySizeMB',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='numCpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='numEthernetCards',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='numVirtualDisks',
            field=models.IntegerField(default=0),
        ),
    ]
