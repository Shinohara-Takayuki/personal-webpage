# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20161118_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='idCategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='page.Category'),
        ),
    ]
