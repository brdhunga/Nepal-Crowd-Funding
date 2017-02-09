from django.shortcuts import render

from django.views.generic import TemplateView

from nepalfund_cms.models import MainPageSettings

from project.models import Project 


class HomepageView(TemplateView):
    template_name = "home/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['settings'] = MainPageSettings.for_site(self.request.site)


def home(request):
    projects = Project.objects.filter(project_status=Project.ACTIVE)
    return render(request, 
                'home/home_page.html',
                {
                    'settings': MainPageSettings.for_site(request.site),
                    'projects': projects}
                )

