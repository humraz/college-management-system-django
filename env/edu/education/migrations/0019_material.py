# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-26 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0018_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to=b'')),
                ('department', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('semester', models.CharField(max_length=30)),
            ],
        ),
    ]