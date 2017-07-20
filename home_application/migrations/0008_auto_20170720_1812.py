# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0007_auto_20170720_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='cluster',
            field=models.ForeignKey(related_name='vcenter_virtualmachine_ref_cluster', to='home_application.VcenterCluster', null=True),
        ),
        migrations.AlterField(
            model_name='vcentervirtualmachine',
            name='datacenter',
            field=models.ForeignKey(related_name='vcenter_virtualmachine_ref_datacenter', to='home_application.VcenterDatacenter', null=True),
        ),
    ]
