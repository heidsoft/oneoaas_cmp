# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0012_auto_20170730_1839'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='vcentervirtualmachinesnapshot',
            table='vcenter_virtualmachine_snapshot',
        ),
    ]
