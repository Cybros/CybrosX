# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0155_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stripecustomer',
            old_name='available_balance',
            new_name='account_balance',
        ),
    ]
