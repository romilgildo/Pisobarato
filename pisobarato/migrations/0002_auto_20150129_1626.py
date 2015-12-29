# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pisobarato', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piso',
            name='fecha_visita',
        ),
        migrations.AddField(
            model_name='piso',
            name='fecha_registro',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha registro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piso',
            name='precio',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
