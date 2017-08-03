# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0017_auto_20170803_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenterhost',
            name='instance_uuid',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
