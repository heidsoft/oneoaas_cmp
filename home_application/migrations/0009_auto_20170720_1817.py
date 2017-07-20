# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0008_auto_20170720_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenterdatastore',
            name='datastoreContainerId',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
    ]
