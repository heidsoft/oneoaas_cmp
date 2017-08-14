# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0020_qcloudimageinfo_qcloudinstanceinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcenteraccount',
            name='account_password',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
    ]
