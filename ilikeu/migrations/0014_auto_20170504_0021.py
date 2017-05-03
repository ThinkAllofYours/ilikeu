# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0013_auto_20170501_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11, unique=True),
        ),
    ]
