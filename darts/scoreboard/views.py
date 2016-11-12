from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from scoreboard.forms import NewEventForm, EventForm, SinglePlayerForm, DoublePlayerForm, TeamPlayerForm, GameScoreForm
from scoreboard.models import Event, Team

# Create your views here.

def test(request):
    return render(request, "base.html")

@login_required(login_url='/accounts/login/')
def new_event(request):
    form = NewEventForm(request.POST or None)
    if form.is_valid():
        instance_home_team = Team.objects.filter(name=request.POST["home_team"])[0]
        instance_away_team = Team.objects.filter(name=request.POST["away_team"])[0]
        event = Event(home_team=instance_home_team, 
                      away_team=instance_away_team)
        event.save()
        return HttpResponseRedirect('/events/{}'.format(event.pk))
    return render(request, "newevent.html", {"form": form})

@login_required(login_url='/accounts/login/')
def view_games(request):
    return render(request, "simple.html", {"header": "view_games", 
                                           "title": "view_games", 
                                           "content": "view_games"})

@login_required(login_url='/accounts/login/')
def view_teams(request):
    return render(request, "simple.html", {"header": "view_teams", 
                                           "title": "view_teams", 
                                           "content": "view_teams"})

@login_required(login_url='/accounts/login/')
def current_event(request, pk):
    event = Event.objects.filter(pk=pk)[0]
    #event = get_object_or_404(Event, pk=pk)
    context = {"event": event}
    if event.complete:
        return render(request, 'eventcomplete.html', context)
    else:
        form_type = EventForm(request.POST or None)
        context = {"form_type": form_type,
                   "event": event}
        if form_type.is_valid():
            if request.POST["game_type"] == 't':
                form_player = TeamPlayerForm(request.POST or None)
                context["form_player"] = form_player
            elif request.POST["game_type"] == 'd':
                form_player = DoublePlayerForm(request.POST or None)
                context["form_player"] = form_player
            elif request.POST["game_type"] == 's':
                form_player = SinglePlayerForm(request.POST or None)
                context["form_player"] = form_player
                
            if form_player.is_valid():
                if form_player == TeamPlayerForm(request.POST or None):
                    team_home = form_player.home
                    team_away = form_player.away
                    players = {}
                players = form_player.cleaned_data
                form_score = GameScoreForm(players, 0, request.POST or None)
                context["form_score"] = form_score
        return render(request, 'editevent.html', context)
    