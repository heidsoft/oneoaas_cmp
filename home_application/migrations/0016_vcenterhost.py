# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0015_auto_20170730_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='VcenterHost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('api_type', models.CharField(default=b'', max_length=20)),
                ('api_version', models.CharField(default=b'', max_length=20)),
                ('build', models.CharField(default=b'', max_length=20)),
                ('full_name', models.CharField(default=b'', max_length=20)),
                ('instance_uuid', models.CharField(default=b'', max_length=20)),
                ('license_product_name', models.CharField(default=b'', max_length=20)),
                ('license_product_version', models.CharField(default=b'', max_length=20)),
                ('locale_build', models.CharField(default=b'', max_length=20)),
                ('locale_version', models.CharField(default=b'', max_length=20)),
                ('os_type', models.CharField(default=b'', max_length=20)),
                ('product_line_id', models.CharField(default=b'', max_length=20)),
                ('vendor', models.CharField(default=b'', max_length=20)),
                ('version', models.CharField(default=b'', max_length=20)),
            ],
            options={
                'db_table': 'vcenter_host',
            },
        ),
    ]
