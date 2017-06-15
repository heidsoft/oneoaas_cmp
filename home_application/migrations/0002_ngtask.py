# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NgTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskName', models.CharField(max_length=127)),
                ('taskResult', models.CharField(max_length=127)),
                ('taskFinishTime', models.DateField()),
            ],
            options={
                'db_table': 'ng_task',
            },
        ),
    ]
