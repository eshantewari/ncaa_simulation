# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_variable_mean'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.IntegerField(default=0),
        ),
    ]
