# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0003_auto_20170331_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='choise1',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='man',
            name='choise2',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='man',
            name='mate_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='man',
            name='number',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='woman',
            name='choise1',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='woman',
            name='choise2',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='woman',
            name='mate_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='woman',
            name='number',
            field=models.SmallIntegerField(),
        ),
    ]
