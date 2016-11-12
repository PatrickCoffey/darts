# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('game_type', models.CharField(default='s', choices=[('t', 'Team'), ('d', 'Doubles'), ('s', 'Singles')], max_length=1)),
                ('event', models.ForeignKey(to='scoreboard.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Game_Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('handicap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('darts', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='scoreboard.Team', related_name='members'),
        ),
        migrations.AddField(
            model_name='game_score',
            name='player',
            field=models.ForeignKey(to='scoreboard.Player'),
        ),
        migrations.AddField(
            model_name='game_score',
            name='scores',
            field=models.ForeignKey(to='scoreboard.Score'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_scores',
            field=models.ForeignKey(to='scoreboard.Game_Score'),
        ),
        migrations.AddField(
            model_name='event',
            name='away_team',
            field=models.ForeignKey(to='scoreboard.Team', related_name='awat_game'),
        ),
        migrations.AddField(
            model_name='event',
            name='home_team',
            field=models.ForeignKey(to='scoreboard.Team', related_name='home_game'),
        ),
    ]
