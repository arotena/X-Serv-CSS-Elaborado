# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procesar', '0002_auto_20160430_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenido',
            old_name='Contenido',
            new_name='contenido',
        ),
    ]