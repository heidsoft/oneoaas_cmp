# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0007_auto_20170620_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vcentervirtualmachine',
            name='guest',
        ),
    ]
