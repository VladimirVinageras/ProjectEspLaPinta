# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('photoUrl', models.CharField(max_length=1024)),
                ('text_preview', models.TextField(default='Put your preview text here')),
                ('text_intro', models.TextField(default='Put your preview text here')),
                ('category', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MenuElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_link', models.CharField(default='Url here', max_length=256)),
                ('level', models.IntegerField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_photoURL', models.URLField()),
                ('opinion', models.TextField()),
            ],
        ),
    ]
