# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_auto_20170901_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contestant',
            new_name='sender',
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to=profiles.models.File.generatePath),
        ),
        migrations.AlterField(
            model_name='message',
            name='review',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
