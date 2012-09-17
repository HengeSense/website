from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.utils.moderator import get_cmsplugin_queryset
from cms.utils import get_language_from_request
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _
from models import FaqEntry, FaqList, FaqEntryLink
from cms.plugins.text.cms_plugins import TextPlugin
from cms.plugins.text.utils import plugin_tags_to_user_html
from django.utils.text import truncate_words
from django.conf import settings

class CMSFaqEntryPlugin(TextPlugin):
    """
	Subclass of Text plugin that includes 'topic' and 'css' fields.
	"""
    model = FaqEntry
    name = _("FAQ Entry")
    render_template = "cms/plugins/faq_entry.html"

    def render(self, context, instance, placeholder):
        context.update({
            "body": plugin_tags_to_user_html(instance.body, context, placeholder),
            "topic": instance.topic,
            "css": instance.get_css_display(),
            "placeholder": placeholder,
            "object": instance,
        })
        return context
plugin_pool.register_plugin(CMSFaqEntryPlugin)

class CMSFaqListPlugin(CMSPluginBase):
    """
    Lists all FaqEntry plugins on the same page as this plugin.
    """
    model = FaqList
    name = _("FAQ List")
    render_template = "cms/plugins/faq_list.html"

    def render(self, context, instance, placeholder):
        request = context.get("request", None)
        if context.has_key("request"):
            lang = get_language_from_request(request)
        else:
            lang = settings.LANGUAGE_CODE

        # Get all FaqEntryPlugins on this page and in this language
        plugins = get_cmsplugin_queryset(request).filter(
            plugin_type="CMSFaqEntryPlugin",
            placeholder__page=instance.page,
            language=lang,
            placeholder__slot__iexact=placeholder,
            parent__isnull=True
        ).order_by("position").select_related()

        faqentry_plugins = []

        # Make a list of the FaqEntry plugin objects
        for plugin in plugins:
            # Truncate the entry's body
            if instance.truncate_body:
                plugin.faqentry.body = truncate_words(plugin.faqentry.body, instance.truncate_body)
            # Show the entry's body or not
            if not instance.show_body:
                plugin.faqentry.body = ''
            faqentry_plugins.append(plugin.faqentry)

        context.update({
            "faq_list": faqentry_plugins,
            "css": instance.get_css_display(),
            "placeholder": placeholder,
        })
        return context
plugin_pool.register_plugin(CMSFaqListPlugin)
