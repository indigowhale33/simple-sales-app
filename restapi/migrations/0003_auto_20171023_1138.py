# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20171023_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(default='', editable=False, to='restapi.Product'),
        ),
    ]
