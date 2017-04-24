# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0005_auto_20170408_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='choise1',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='choise2',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='mate_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
