from django.conf.urls import patterns, include, url
from agronomia_pbd import views
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^register/$', views.register),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    
)
