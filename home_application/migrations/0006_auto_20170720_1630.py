# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_auto_20170720_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcentercluster',
            name='actionHistoryNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcentercluster',
            name='drsRecommendationNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcentercluster',
            name='enabledClusterHa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vcentercluster',
            name='migrationHistoryNum',
            field=models.IntegerField(default=0),
        ),
    ]
