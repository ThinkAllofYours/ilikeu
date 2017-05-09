# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0020_auto_20170506_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ('-mate_date', '-mate_seq', '-gender', '-number')},
        ),
        migrations.RenameField(
            model_name='matedates',
            old_name='isComplete',
            new_name='end_choice',
        ),
        migrations.RenameField(
            model_name='matedates',
            old_name='isOpen',
            new_name='start_choice',
        ),
    ]
