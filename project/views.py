from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Project


class ProjectsListView(ListView):
	model = Project