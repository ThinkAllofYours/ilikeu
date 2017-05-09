# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0017_human_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='mate_seq',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matedates',
            name='mate_seq',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
