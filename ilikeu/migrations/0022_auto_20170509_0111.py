# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0021_auto_20170509_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='phoneNumber',
            field=models.CharField(max_length=11),
        ),
    ]
