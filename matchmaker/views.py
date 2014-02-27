from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from matchmaker.models import Team
from django.core.context_processors import csrf
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def team_index(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {"teams": teams})


def detail(request, league):
    #Check if ALL, if so display all teams
    if league == "A":
        teams = Team.objects.all()
    elif league:
        teams = Team.objects.filter(league=league)
    return render(request, 'teams.html', {"teams": teams})


def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team_detail.html', {"team": team})


def auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
