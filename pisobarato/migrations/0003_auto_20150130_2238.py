# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pisobarato', '0002_auto_20150129_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenes',
            old_name='model_pic',
            new_name='pic',
        ),
    ]
