"""attic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'attic.views.log_in', name='login'),
    url(r'^home/', 'attic.views.home', name='home'),
    url(r'^logout/', 'attic.views.log_out', name='logout'),
    url(r'^profile/(?P<session_id>.*)$', 'attic.views.profile', name='profile'),
    url(r'^reset-session/', 'attic.views.reset_session', name='reset_session'),
    url(r'^delete-session/(?P<session_id>.*)$', 'attic.views.delete_session', name='delete_session'),
    url(r'^delete-query/(?P<query_id>.*)$', 'attic.views.delete_query', name='delete_query'),
    url(r'^delete-query-from-profile/(?P<query_id>.*)$', 'attic.views.delete_query_from_profile', name='delete_query'),
    url(r'^modify/', 'attic.views.modify', name='modify'),
]
