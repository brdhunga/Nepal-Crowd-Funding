from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from .views import (ProjectsListView, ProjectDetailView, 
					ProjectCreateView)

from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', ProjectsListView.as_view(), name="all_projects"),
    # single project 
    url(r'^(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(), 
    						name="single_project"),
    url(r'^new$', login_required(ProjectCreateView.as_view()), name="new_project"),

]

