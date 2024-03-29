# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-26 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoted_by', models.CharField(max_length=45)),
                ('message', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('cpassword', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='users_who_create',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_who_create', to='first_app.users'),
        ),
        migrations.AddField(
            model_name='messages',
            name='users_who_favorite',
            field=models.ManyToManyField(related_name='users_who_favorite', to='first_app.users'),
        ),
    ]
