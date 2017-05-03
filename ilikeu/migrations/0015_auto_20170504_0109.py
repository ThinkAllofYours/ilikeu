# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0014_auto_20170504_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='phoneNumber',
            field=models.CharField(max_length=11, blank=True),
        ),
    ]
