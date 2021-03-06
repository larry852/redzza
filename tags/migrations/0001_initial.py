# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TagProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.Profile')),
                ('tag', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='tags.Tag')),
            ],
        ),
    ]
