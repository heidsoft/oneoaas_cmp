# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_vcentervirtualmachine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='power_state',
            field=models.CharField(max_length=10),
        ),
    ]
