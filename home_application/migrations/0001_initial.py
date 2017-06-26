# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VcenterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_name', models.CharField(max_length=60)),
                ('account_password', models.CharField(max_length=20)),
                ('vcenter_host', models.CharField(max_length=30)),
                ('vcenter_port', models.IntegerField(max_length=10)),
                ('vcenter_version', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'vcenter_account',
            },
        ),
        migrations.CreateModel(
            name='VcenterVirtualMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('vm_pathname', models.CharField(max_length=120)),
                ('guest_fullname', models.CharField(max_length=60)),
                ('power_state', models.CharField(max_length=50)),
                ('ipaddress', models.CharField(max_length=30)),
                ('instance_uuid', models.CharField(max_length=40)),
                ('boot_time', models.TimeField(max_length=20, null=True)),
                ('account', models.ForeignKey(related_name='vcenter_virtualmachine_ref_account', to='home_application.VcenterAccount')),
            ],
            options={
                'db_table': 'vcenter_virtualmachine',
            },
        ),
    ]
