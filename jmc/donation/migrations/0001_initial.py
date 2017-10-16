# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-29 09:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated At')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number mustbe entered in the format: '9999999999'. Only digits allowed.", regex='^\\d{10}$')])),
                ('amount', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_donation_set+', to='account.UserProfile', verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_donation_set+', to='account.UserProfile', verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]