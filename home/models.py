from django.db import models
from wagtail.admin.panels import InlinePanel

from wagtail.models import Page, Orderable
from wagtail.models import TranslatableMixin
from modelcluster.fields import ParentalKey
from app_misc_orderables.models import ContactPerson

# Orderable needs to be TranslatableMixin to be correctly displayed.
class ContactPersonOrderable(Orderable, ContactPerson):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='contact_persons')

    def __str__(self):
        return self.page.title + " -> " + self.contact_person.first_name + " " + self.contact_person.last_name


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('contact_persons', label="Kontaktpersonen"),
    ]
