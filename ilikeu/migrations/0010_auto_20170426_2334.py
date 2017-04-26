# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0009_auto_20170425_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='choise1',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='human',
            name='choise2',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
    ]
