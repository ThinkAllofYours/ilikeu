# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0015_auto_20170504_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateDates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('mate_date', models.DateField(blank=True)),
                ('isOpen', models.BooleanField(default=False)),
                ('isComplete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-mate_date',),
            },
        ),
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ('-mate_date', '-gender', '-number')},
        ),
    ]
