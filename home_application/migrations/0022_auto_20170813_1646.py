# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0021_auto_20170811_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcloudinstanceinfo',
            name='cpu',
            field=models.IntegerField(verbose_name='cpu'),
        ),
        migrations.AlterField(
            model_name='qcloudinstanceinfo',
            name='memory',
            field=models.IntegerField(verbose_name='\u5185\u5b58'),
        ),
    ]
