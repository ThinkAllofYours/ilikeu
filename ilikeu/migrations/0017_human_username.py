# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0016_auto_20170504_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='userName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
