# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWebsite', '0007_menuelement_url_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_intro',
            field=models.TextField(default='Put your preview text here'),
        ),
    ]