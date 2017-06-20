# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20170620_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='vm_pathname',
            field=models.CharField(max_length=120),
        ),
    ]
