# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ilikeu', '0010_auto_20170426_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
