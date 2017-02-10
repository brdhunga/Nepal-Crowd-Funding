from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView

from .models import Project


class ProjectsListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)
        context['objects'] = Project.objects.get_active_projects()
        return context


class ProjectDetailView(DetailView):
    model = Project
    slug_field = 'slug'


class ProjectCreateView(CreateView):
	model = Project
	success_url = '/'