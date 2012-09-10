from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from django.conf import settings
from django.utils.text import truncate_words
from django.conf import settings
from cms.plugins.text.models import AbstractText


#get custom css from settings or use default
CMSPLUGIN_FAQENTRY_CSS_CHOICES = getattr(settings,"CMSPLUGIN_FAQENTRY_CSS_CHOICES", (('1', 'featured'),) )

class FaqEntry(AbstractText):
    """Subclass of Text plugin model, plus additional 'topic' & 'css' fields"""
    topic = models.CharField(_("Topic"),max_length=500, help_text=_('FAQ entry topic'))
    css = models.CharField(_('CSS class'), max_length=1, choices=CMSPLUGIN_FAQENTRY_CSS_CHOICES, blank=True, help_text=_('Additional CSS class to apply'))

    search_fields = ('topic', 'body',)

    def __unicode__(self):
        return u"%s" % (truncate_words(self.topic, 5)[:30]+"...")


#get custom css from settings or use default
CMSPLUGIN_FAQLIST_CSS_CHOICES = getattr(settings,"CMSPLUGIN_FAQLIST_CSS_CHOICES", (('1', 'faq-list'),('2', 'faq-list-small'),) )

class FaqList(CMSPlugin):
    """Model to give FaqList plugin various options"""
    truncate_body = models.PositiveSmallIntegerField(_('Truncate words'), default=5, help_text=_('Truncate FAQ Entry body by this many words; zero means Django default'))
    show_body = models.BooleanField(_('Show FAQ Entry body'),default=True)
    css = models.CharField(_('CSS class'), max_length=1, choices=CMSPLUGIN_FAQLIST_CSS_CHOICES, blank=True, help_text=_('Additional CSS class to apply'))

    def __unicode__(self):
        return u"%s" % (self.page.get_page_title())

#get custom css from settings or use default
CMSPLUGIN_FAQENTRYLINK_CSS_CHOICES = getattr(settings,"CMSPLUGIN_FAQENTRYLINK_CSS_CHOICES", (('1', 'faq-entry-link-small'),) )

class FaqEntryLink(CMSPlugin):
    """Model to give FaqEntryLink plugin various options"""
    link = models.ForeignKey(FaqEntry, blank=True, null=True, verbose_name=_('Linked FAQ Entry'), help_text=_('Leave empty for random'))
    truncate_body = models.PositiveSmallIntegerField(_('Truncate words'), default=5, help_text=_('Truncate FAQ Entry body by this many words; zero means Django default'))
    show_body = models.BooleanField(_('Show FAQ Entry body'),default=True)
    css = models.CharField(_('CSS class'), max_length=1, choices=CMSPLUGIN_FAQENTRYLINK_CSS_CHOICES, blank=True, help_text=_('Additional CSS class to apply'))

    def __unicode__(self):
        return u"FAQ Entry %s" % (self.link)