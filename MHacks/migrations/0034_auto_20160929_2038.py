# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-30 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MHacks', '0033_auto_20160929_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='acceptance',
            field=models.CharField(choices=[(b'accepted_yes', b'HAIL YEAH! \xf0\x9f\x98\x80'), (b'accepted_no', b"No, I can't make it \xf0\x9f\x98\xad")], max_length=32),
        ),
    ]
