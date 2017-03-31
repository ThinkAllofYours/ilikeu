# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('mate_date', models.DateTimeField()),
                ('phoneNumber', models.CharField(max_length=11)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('choise1', models.IntegerField()),
                ('choise2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('mate_date', models.DateTimeField()),
                ('phoneNumber', models.CharField(max_length=11)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('choise1', models.IntegerField()),
                ('choise2', models.IntegerField()),
            ],
        ),
    ]
