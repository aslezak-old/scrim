from django.shortcuts import render, render_to_response
from matchmaker.models import Team
from django.http import HttpResponse
# Create your views here.


def index(request):
    teams = Team.objects.all()
    return render(request, 'index.html', {'teams': teams})


def detail(request):
    return HttpResponse("WORKED")