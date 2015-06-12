from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='index.html'),  name='index'),
    #url(r'^$', include('polls.urls', namespace="polls")),

    url(r'^accounts/',
        include('registration.backends.default.urls')),

    #url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^accounts/profile/', include('polls.urls', namespace="polls"), name='profile'),
        
    #url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^login/',
        'django.contrib.auth.views.login',
        name='login'),

    url(r'^admin/', include(admin.site.urls))
)