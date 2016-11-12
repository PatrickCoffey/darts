from django.db import models

import datetime

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    #members = models.ForeignKey(Player)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name   
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    handicap = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name 
    
class Score(models.Model):
    darts = models.IntegerField()
    value = models.IntegerField()

class Game_Score(models.Model):
    player = models.ForeignKey(Player)
    turn = models.IntegerField()
    scores = models.ForeignKey(Score)

class Event(models.Model):
    event_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    home_team = models.ForeignKey(Team, related_name="home_game")
    away_team = models.ForeignKey(Team, related_name="away_game")
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        title = str(self.home_team) + " vs. "
        title += str(self.away_team) + " - "
        title += self.event_date.strftime("%x")
        return title
    
    def __unicode__(self):
        self.__str__()

class Game(models.Model):
    GAME_TYPES = (('t', 'Team'), ('d', 'Doubles'), ('s', 'Singles'))
    date = models.DateField()
    game_type = models.CharField(max_length=1, choices=GAME_TYPES, default='s')
    player_scores = models.ManyToManyField(Game_Score)
    event = models.ForeignKey(Event)