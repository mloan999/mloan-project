# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0003_remove_loan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='enter_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
