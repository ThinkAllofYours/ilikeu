# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0012_auto_20170426_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='human',
            old_name='choise1',
            new_name='choice1',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='choise2',
            new_name='choice2',
        ),
    ]
