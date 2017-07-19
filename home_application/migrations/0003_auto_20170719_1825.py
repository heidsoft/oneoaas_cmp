# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20170719_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='numCpu',
            field=models.IntegerField(max_length=20),
        ),
    ]
