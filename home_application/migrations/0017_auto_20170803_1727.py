# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0016_vcenterhost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenterhost',
            name='full_name',
            field=models.CharField(default=b'', max_length=60),
        ),
    ]
