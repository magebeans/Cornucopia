# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-22 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.CharField(max_length=256),
        ),
    ]
