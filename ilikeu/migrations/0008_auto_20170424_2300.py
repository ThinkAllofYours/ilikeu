# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0007_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='choise1',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='choise2',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
