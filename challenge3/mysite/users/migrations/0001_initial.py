# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name=b'Last Name', blank=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
