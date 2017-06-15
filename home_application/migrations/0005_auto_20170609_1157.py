# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacturer',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]
