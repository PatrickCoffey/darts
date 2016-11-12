from django import forms
from django.contrib.auth.admin import User

from bootstrap3_datetime.widgets import DateTimePicker

from scoreboard.models import Player, Team, Event, Game, Score

#class EventModelForm(forms.ModelForm):
    #class Meta:
        #model = Event

class NewEventForm(forms.Form):
    TEAMS = zip(Team.objects.all(), Team.objects.all())
    TEAMS2 = zip(Team.objects.all(), Team.objects.all())
    home_team = forms.ChoiceField(choices=TEAMS, widget=forms.RadioSelect)
    away_team = forms.ChoiceField(choices=TEAMS2, widget=forms.RadioSelect)

class NewGameForm(forms.Form):
    game_time = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY HH:mm",
                                                                   "pickTime": True}))
    choices = zip(Player.objects.all(), Player.objects.all())
    players = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, 
                                        choices=choices)
    
class EventForm(forms.Form):
    GAME_TYPES = (('t', 'Team'), ('d', 'Doubles'), ('s', 'Singles'))
    game_type = forms.ChoiceField(choices=GAME_TYPES)

class DoublePlayerForm(forms.Form):
    PLAYERS = Player.objects.all()
    home_1 = forms.ModelChoiceField(PLAYERS)
    home_2 = forms.ModelChoiceField(PLAYERS)
    away_1 = forms.ModelChoiceField(PLAYERS)
    away_2 = forms.ModelChoiceField(PLAYERS)
    
class SinglePlayerForm(forms.Form):
    PLAYERS = Player.objects.all()
    home_1 = forms.ModelChoiceField(PLAYERS)
    home_2 = forms.ModelChoiceField(PLAYERS, required=False)
    home_3 = forms.ModelChoiceField(PLAYERS, required=False)
    home_4 = forms.ModelChoiceField(PLAYERS, required=False)
    home_5 = forms.ModelChoiceField(PLAYERS, required=False)
    away_1 = forms.ModelChoiceField(PLAYERS)
    away_2 = forms.ModelChoiceField(PLAYERS, required=False)
    away_3 = forms.ModelChoiceField(PLAYERS, required=False)
    away_4 = forms.ModelChoiceField(PLAYERS, required=False)
    away_5 = forms.ModelChoiceField(PLAYERS, required=False)
    
class TeamPlayerForm(forms.Form):
    TEAMS = Team.objects.all()
    home = forms.ModelChoiceField(TEAMS)
    away = forms.ModelChoiceField(TEAMS)
    
class GameScoreForm(forms.Form):
    teams = {"home": {"players": {}},
             "away": {"players": {}}}
    def __init__(self, teams, n,  *args, **kwargs):
        super(GameScoreForm, self).__init__(*args, **kwargs)
        for name, team in teams.items():
            self.fields["{}_score_{}".format(player, n+1)] = forms.IntegerField(label="{} Score ({})".format(n+1, player))
            self.fields["{}_darts_{}".format(player, n+1)] = forms.IntegerField(label="{} Darts ({})".format(n+1, player))