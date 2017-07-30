# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0009_auto_20170720_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='VcenterVirtualMachineSnapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='\u5feb\u7167\u540d\u79f0')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='\u5feb\u7167\u63cf\u8ff0')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('result', models.CharField(default=b'running', max_length=20, verbose_name='\u521b\u5efa\u5feb\u7167\u7ed3\u679c:running\u8868\u793a\u6b63\u5728\u521b\u5efa\u4e2d\uff0csuccess\u8868\u793a\u521b\u5efa\u5feb\u7167\u6210\u529f\uff0cfailed\u8868\u793a\u521b\u5efa\u5931\u8d25')),
                ('account', models.ForeignKey(related_name='vcenter_virtualMachine_napshot_ref_account', to='home_application.VcenterAccount')),
                ('virtualmachine', models.ForeignKey(related_name='vcenter_virtualMachine_napshot_ref_virtualmachine', to='home_application.VcenterVirtualMachine')),
            ],
            options={
                'db_table': 'vcenter_virtualMachine_snapshot',
            },
        ),
        migrations.RemoveField(
            model_name='vcenternetwork',
            name='datacenter',
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='host',
            field=models.CharField(default=b'', max_length=32),
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='mtu',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='num_ports',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='num_ports_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='portgroup',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='vcenternetwork',
            name='vnic',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vcenternetwork',
            name='name',
            field=models.CharField(default=b'', max_length=60),
        ),
    ]
