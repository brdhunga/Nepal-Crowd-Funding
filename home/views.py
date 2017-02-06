from django.shortcuts import render

from django.views.generic import TemplateView

from nepalfund_cms.models import MainPageSettings


class HomepageView(TemplateView):
    template_name = "home/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['settings'] = MainPageSettings.for_site(self.request.site)


def home(request):
    return render(request, 
                'home/home_page.html',
                {'settings': MainPageSettings.for_site(request.site)}
                )

