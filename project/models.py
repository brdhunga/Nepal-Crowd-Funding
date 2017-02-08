from django.db import models
from django.conf import settings

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from ckeditor.fields import RichTextField


class Project(models.Model):
    """
    Project model. This stores direct information and metadata about
    the project.
    
    Note that there are various levels of a project lifecycle
    DRAFTED -> made by an end user 
    STAGED -> technically correct but is not visible to public for 
            political government reasons such as validity and the conscience
    ACTIVE -> visible to end user and users can donate
    COMPLETED -> done. visible to public but they cannot fund it. 
    """
    DRAFTED = 'DR'
    STAGED = 'ST'
    ACTIVE = 'AC'
    COMPLETED = 'CO'
    
    PROJECT_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (STAGED, 'Staged'),
        (COMPLETED, 'Completed'),
        (DRAFTED, 'Drafted'),
    )

    PROJECT_ENDING_STATEMENT = "Only hours left"
    PROJECT_ENDED_STATEMENT = "Peoject deadline reached"

    funding_goal = models.DecimalField(
        max_digits = 15,
        decimal_places = 2,
        help_text = "How much do you aim to raise for the project?"
    )
    title = models.CharField(
        max_length=255,
        help_text='What would you like to name this project?'
    )
    tagline = models.CharField(
        max_length=200,
        null=True,
        blank=False,
        help_text='Write a short tag line that describes this project.)'
    )
    video_url = models.URLField(
        'Video URL',
        max_length=255,
        blank=True,
        help_text='Optional: Link to a Youtube or vimeo about the project.'
    )
    location = models.CharField(
        'Organization Address',
        max_length=255,
        help_text='What is the address of the organization or main site of the project?'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateField(
        help_text='When will this crowdfunding project end?'
    )
    # this has to be set dynamically
    start_date = models.DateField(
        blank=True,
        null=True
    )
    project_status = models.CharField(
        max_length=2,
        choices=PROJECT_STATUS_CHOICES,
        default=DRAFTED
    )
    cover_photo = ProcessedImageField(
        upload_to='covers/',
        processors=[ResizeToFill(1200, 500)],
        format='JPEG',
        options={'quality': 60},
        default=None,
        help_text='A high resolution image to represent the project.',
        blank=True
    )
    preview_photo = ImageSpecField(
        source='cover_photo',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 80},
    )
    description = RichTextField(
        'Project description',
        help_text='This is the body of content that shows up on the project page.'
    )
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by_user')

    def get_owner(self):
        return self.created_by_user

    def check_if_owner(self, user):
        return self.created_by_user == user

    def __str__(self):
        return self.title
















