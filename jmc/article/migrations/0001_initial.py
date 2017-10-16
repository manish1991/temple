# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-29 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('media', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated At')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('snippet_text', models.TextField()),
                ('url', models.CharField(blank=True, max_length=255)),
                ('url_slug', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField(blank=True)),
                ('video_link', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('search_text', models.CharField(blank=True, max_length=255)),
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('api_calls', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.ArticleState'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='cover_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_article_set+', to='account.UserProfile', verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_article_set+', to='account.UserProfile', verbose_name='Updated By'),
        ),
    ]