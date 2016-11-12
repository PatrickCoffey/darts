# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
