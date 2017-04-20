# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PRODUCE', 'Produce'), ('MEAT/SEAFOOD', 'Meat/Seafood'), ('DAIRY', 'Dairy'), ('FROZEN FOODS', 'Frozen Foods'), ('BREADS/PASTAS', 'Breads/Pasta'), ('CANNED GOODS', 'Canned Goods'), ('BREAKFAST', 'Breakfast'), ('SNACKS', 'Snacks'), ('BAKING/CONDIMENTS', 'Baking/Condiments'), ('BEVERAGES', 'Beverages'), ('PAPER/PLASTIC', 'Paper/Plastic'), ('CLEANING PRODUCTS', 'Cleaning Products'), ('TOILETRIES', 'Toiletries'), ('MISC', 'Miscellaneous')], max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
    ]
