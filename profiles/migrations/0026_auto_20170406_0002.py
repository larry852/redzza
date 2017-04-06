# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0025_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(b'F', b'Femenino'), (b'M', b'Masculino')], default=b'M', max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
