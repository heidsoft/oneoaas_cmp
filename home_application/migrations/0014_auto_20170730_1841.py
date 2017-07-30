# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0013_auto_20170730_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='instance_uuid',
            field=models.CharField(unique=True, max_length=40),
        ),
    ]
