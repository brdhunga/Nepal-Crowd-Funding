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



@register_setting
class MainPageSettings(BaseSetting):
    """
    """
    site_tagline = models.CharField(
        max_length=100,
        help_text="The tagline for the site.",
        default="LETS START FUNDING THE NEW NEPAL."
    )
    site_subheading = models.TextField(
        help_text="Sub heading for the site",
        default="When you donate to nepal fund's projects, you are making a lasting impact on the future of Nepal."
    )
    learn_button_text = models.CharField(
        max_length=50,
        help_text="The label on the 'Learn more button'",
        default="DONATE"
    )
    how_it_works_heading = models.CharField(
        max_length=50,
        help_text="The heading to display above the 'Learn about how it works' section ",
        default="How it works"
    )
    how_it_works_intro = models.TextField(
        help_text="Intro paragraph for the 'Learn about how it works' section.",
        default=(
            "'What a piece of work is man! how noble in reason! how infinite in faculty! in form and moving how express and admirable! in action how like an angel! in apprehension how like a god! the beauty of the world, the paragon of animals! '. - (Act II, Scene II)."
       )
    )
    how_it_works_video_url = models.URLField(help_text="URL for 'how it works' video", default="https://www.youtube.com/embed/MCJGcDDNtms")

    
