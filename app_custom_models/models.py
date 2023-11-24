from django.db import models
from django.utils.translation import gettext as _

from wagtail.admin.panels import FieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet

from wagtail.search import index
from wagtail.models import TranslatableMixin


@register_snippet
class ContactPersonModel(index.Indexed, TranslatableMixin, models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    further_information = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel('image', heading='Profilbild'),
        FieldRowPanel(
            [
                FieldPanel('first_name', heading='Vorname'), 
                FieldPanel('last_name', heading='Nachname')
            ], 
            classname='name'
        ),
        FieldPanel('further_information')
    ]

    search_fields = [
        # Filters in SnippetChooser
        index.FilterField('locale_id'),
        index.FilterField('last_name', partial_match=True),
        index.FilterField('first_name', partial_match=True),

        # Search in WagtailAdmin Snippets
        index.AutocompleteField('last_name'),
        index.AutocompleteField('first_name'),
    ]

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta(TranslatableMixin.Meta):     # noqa
        verbose_name = _("Contact person")
        verbose_name_plural = _("Contact persons")
