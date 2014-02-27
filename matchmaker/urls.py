from django.conf.urls import patterns, url

from matchmaker import views

urlpatterns = patterns('',
    url(r'^$', 'matchmaker.views.team_index', name='teams'),
    url(r'^(?P<league>[A-Z])/$', 'matchmaker.views.detail', name='detail'),
    url(r'^(?P<team_id>\d+)/$', 'matchmaker.views.team_detail', name='team_detail'),
)