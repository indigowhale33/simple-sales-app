# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_auto_20171026_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='restapi.Cart'),
        ),
    ]
