from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import ProjectsListView, ProjectDetailView


urlpatterns = [
    url(r'^$', ProjectsListView.as_view(), name="all_projects"),
    # single project 
    url(r'^(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(), name="single_project"),
]

