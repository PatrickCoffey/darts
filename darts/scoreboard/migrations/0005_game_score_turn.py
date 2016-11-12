# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_auto_20161112_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_score',
            name='turn',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
