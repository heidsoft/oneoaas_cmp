# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0018_auto_20170803_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcenteraccount',
            name='cloud_private_key',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='vcenteraccount',
            name='cloud_provider',
            field=models.CharField(default=b'', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vcenteraccount',
            name='cloud_public_key',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='vcenteraccount',
            name='project_id',
            field=models.CharField(default=b'', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='account_password',
            field=models.CharField(default=b'', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='vcenter_host',
            field=models.CharField(default=b'', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='vcenter_port',
            field=models.IntegerField(default=443, null=True),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='vcenter_version',
            field=models.CharField(default=b'', max_length=10, null=True),
        ),
    ]
