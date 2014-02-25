from django.conf.urls import patterns, url

from matchmaker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/team/(?P<team_id>\d+)/$', views.detail, name='detail'),
)