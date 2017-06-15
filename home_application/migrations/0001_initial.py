# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NgUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=127)),
                ('age', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'ng_user',
            },
        ),
    ]
