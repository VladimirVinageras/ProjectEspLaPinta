# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWebsite', '0003_auto_20171015_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photoUrl',
            field=models.CharField(max_length=1024),
        ),
    ]