# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0004_conversation_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.File.generatePath),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
