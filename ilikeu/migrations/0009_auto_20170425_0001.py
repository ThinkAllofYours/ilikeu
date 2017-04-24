# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0008_auto_20170424_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('gender', models.CharField(choices=[('M', 'MAN'), ('W', 'WOMAN')], default='M', max_length=1)),
                ('mate_date', models.DateField(blank=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=11)),
                ('password', models.CharField(max_length=20)),
                ('number', models.SmallIntegerField()),
                ('choise1', models.SmallIntegerField(blank=True)),
                ('choise2', models.SmallIntegerField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
