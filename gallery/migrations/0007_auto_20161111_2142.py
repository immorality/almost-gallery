# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-11 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20161111_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='./static/images'),
        ),
    ]
