# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0014_auto_20170730_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenternetwork',
            name='portgroup',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]
