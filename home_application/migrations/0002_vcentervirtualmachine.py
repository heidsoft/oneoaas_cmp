# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VcenterVirtualMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('vm_pathname', models.CharField(max_length=20)),
                ('guest_fullname', models.CharField(max_length=30)),
                ('power_state', models.IntegerField(max_length=10)),
                ('guest', models.CharField(max_length=10)),
                ('ipaddress', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'vcenter_virtualmachine',
            },
        ),
    ]
