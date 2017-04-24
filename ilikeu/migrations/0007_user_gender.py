# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0006_auto_20170410_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'MAN'), ('W', 'WOMAN')], default='M'),
        ),
    ]
