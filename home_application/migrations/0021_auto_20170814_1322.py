# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0020_auto_20170814_1307'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ucloudinstance',
            table='ucloud_instance_info',
        ),
    ]
