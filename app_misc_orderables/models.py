from django.db import models
from django.utils.translation import gettext as _
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin, BootstrapTranslatableMixin

""" Contact person abstract """
class ContactPerson(models.Model):
    contact_person = models.ForeignKey('app_custom_models.ContactPersonModel', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = _("Contact person")
        verbose_name_plural = _("Contact persons")
        abstract = True

    panels = [
        FieldPanel('contact_person', heading=_("Contact person")),
    ]
