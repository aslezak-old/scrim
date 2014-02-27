from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'matchmaker.views.index', name='index'),
    url(r'^teams/', include('matchmaker.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', 'matchmaker.views.auth', name='auth_view'),
    url(r'^logout/$', 'matchmaker.views.logout_view', name='logout_view'),

)
