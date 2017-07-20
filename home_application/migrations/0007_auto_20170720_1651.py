# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0006_auto_20170720_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcenterdatastore',
            name='accessible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='datastoreContainerId',
            field=models.CharField(default=b'', max_length=60),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='filesystemType',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='freeSpace',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='maintenanceMode',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='mountHostNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='multipleHostAccess',
            field=models.BooleanField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vcenterdatastore',
            name='url',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]
