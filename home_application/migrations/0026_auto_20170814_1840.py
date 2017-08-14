# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0025_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcenteraccount',
            name='cloud_region',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='\u4e91\u533a\u57df'),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='cloud_private_key',
            field=models.CharField(default=b'', max_length=60, null=True, verbose_name='\u4e91\u79c1\u94a5\u5319'),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='cloud_provider',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='\u4e91\u63d0\u4f9b\u5546'),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='cloud_public_key',
            field=models.CharField(default=b'', max_length=60, null=True, verbose_name='\u4e91\u516c\u94a5\u5319'),
        ),
        migrations.AlterField(
            model_name='vcenteraccount',
            name='project_id',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='\u4e91\u9879\u76ee'),
        ),
    ]
