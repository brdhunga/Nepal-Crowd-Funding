from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import ProjectsListView


urlpatterns = [
    url(r'^$', ProjectsListView.as_view(), name="all_projects")
]

