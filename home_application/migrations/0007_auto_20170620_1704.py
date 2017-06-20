# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0006_auto_20170620_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='guest',
            field=models.CharField(max_length=200),
        ),
    ]
