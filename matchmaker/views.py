from django.shortcuts import render, render_to_response
from matchmaker.models import Team
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def team_index(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {"all_teams": teams})


def detail(request, league):
    #Check if ALL, if so display all teams
    if league == "A":
        teams = Team.objects.all()
    elif league:
        teams = Team.objects.filter(league=league)
    return render(request, 'teams.html', {"teams": teams})
