# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0022_auto_20170509_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='mate_seq',
            field=models.SmallIntegerField(default=1, blank=True, null=True),
        ),
    ]
