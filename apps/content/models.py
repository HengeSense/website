
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.galleries.models import Gallery

class CustomGallery(Gallery):
	"""
	Implements a custom gallery with a subtitle.
	"""
	subtitle = models.CharField(_("Subtitle"), max_length=500)

	search_fields = ("subtitle", "content")

	class Meta:
		verbose_name = _("Custom gallery")
		verbose_name_plural = _("Custom galleries")
	
class SubtitleRichTextPage(Page, RichText):
	"""
	Implements a type of page with a single Rich Text content field
	and a subtitle.
	"""
	subtitle = models.CharField(_("Subtitle"), max_length=500)

	search_fields = ("subtitle", "content")

	class Meta:
		verbose_name = _("Rich text page with subtitle")
		verbose_name_plural = _("Rich text pages with subtitle")
