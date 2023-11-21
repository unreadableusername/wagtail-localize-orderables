from django.db import models
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin

""" Contact person abstract """
class ContactPerson(models.Model):
    contact_person = models.ForeignKey('app_custom_models.ContactPersonModel', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Kontaktperson"
        verbose_name_plural = "Kontaktpersonen"
        abstract = True

    panels = [
        FieldPanel('contact_person', heading="Kontaktperson"),
    ]
