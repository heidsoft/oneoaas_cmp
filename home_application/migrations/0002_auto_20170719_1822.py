# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='guestId',
            field=models.CharField(default="", max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='instanceUuid',
            field=models.CharField(default="", max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='maxCpuUsage',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='maxMemoryUsage',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='memorySizeMB',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='numCpu',
            field=models.IntegerField(default=0,max_length=20),
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='numEthernetCards',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='numVirtualDisks',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='overallStatus',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vcentervirtualmachine',
            name='template',
            field=models.BooleanField(default=False, max_length=1),
            preserve_default=False,
        ),
    ]
