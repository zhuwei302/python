# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_current_price_of_low_rate_stock_fen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock_Fen',
            new_name='Stock_Fenshi',
        ),
    ]
