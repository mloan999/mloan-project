# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_loan_select_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='employee_type',
            field=models.CharField(blank=True, choices=[('Salaried', 'Salaried'), ('Self Employed', 'Self Employed')], max_length=10),
        ),
    ]
