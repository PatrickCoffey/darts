# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_auto_20161112_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='away_team',
            field=models.ForeignKey(related_name='away_game', to='scoreboard.Team'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='player_scores',
        ),
        migrations.AddField(
            model_name='game',
            name='player_scores',
            field=models.ManyToManyField(to='scoreboard.Game_Score'),
        ),
    ]
