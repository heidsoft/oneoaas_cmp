# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_auto_20170720_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='clusterNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='datastoreNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='datastoreTotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='hostNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='networkNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vcenterdatacenter',
            name='vmNum',
            field=models.IntegerField(default=0),
        ),
    ]
