# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-04 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
        ('users', '0014_auto_20161017_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bus_route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bus.Route'),
        ),
    ]
