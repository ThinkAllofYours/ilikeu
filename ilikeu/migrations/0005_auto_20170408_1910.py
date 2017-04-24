# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0004_auto_20170407_0155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Woman',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Man',
        ),
    ]
