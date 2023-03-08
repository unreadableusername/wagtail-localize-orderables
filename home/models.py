from django.db import models
from wagtail.admin.panels import InlinePanel

from wagtail.models import Page, Orderable
from wagtail.models import TranslatableMixin
from modelcluster.fields import ParentalKey

class ContactPersonOrderable(TranslatableMixin, Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='contact_persons')
    person = models.ForeignKey('app_custom_models.ContactPerson', on_delete=models.CASCADE, related_name='+')

    class Meta(TranslatableMixin.Meta ,Orderable.Meta):
        pass

class HomePage(Page):

    content_panels = Page.content_panels + [
        InlinePanel('contact_persons', label="Kontaktpersonen"),
    ]
