# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_pic', models.ImageField(upload_to='static/img/', default='pic_folder/None/no-img.jpg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=10, choices=[('PISO', 'Piso'), ('HABITACION', 'Habitacion')])),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('direccion', models.CharField(max_length=200)),
                ('fecha_visita', models.DateTimeField(verbose_name='Fecha visita')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagenes',
            name='piso',
            field=models.ForeignKey(null=True, to='pisobarato.Piso', blank=True),
            preserve_default=True,
        ),
    ]
