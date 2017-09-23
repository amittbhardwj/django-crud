# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-22 16:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20170922_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='telephone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
