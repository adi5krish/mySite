# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0008_auto_20171029_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterNo',
            field=models.IntegerField(default='', max_length=20),
        ),
    ]