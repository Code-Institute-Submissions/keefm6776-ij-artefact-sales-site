# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-17 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]