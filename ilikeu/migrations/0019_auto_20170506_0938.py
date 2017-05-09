# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0018_auto_20170506_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='phoneNumber',
            field=models.CharField(blank=True, unique=True, max_length=11),
        ),
    ]
