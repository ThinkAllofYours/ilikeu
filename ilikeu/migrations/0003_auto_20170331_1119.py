# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0002_man_woman'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='woman',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
