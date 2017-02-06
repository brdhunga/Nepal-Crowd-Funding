from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.contrib.settings.models import BaseSetting, register_setting


class NepalFundCustomPage(Page):
    """
    A cms page that allows admins to dynamically create 'static' pages
    such as about is, announcements, news updates etc. 

    Models inheriting from Page autmatically get added to wagtail 
    models on admin
    """
    body = RichTextField()
    search_name = "Custom Page"

    indexed_fields = ('body',)
    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full")
    ]


class NepalFundLinkPage(Page):
    """
    A page that represents link to another page. In another words, 
    a dummy page that just forwards to another page. 
    """
    link_href = models.CharField(max_length=1024, blank=True, default='')
    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('link_href', classname="full")
    ]



