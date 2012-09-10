from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _
from models import FaqEntry, FaqList, FaqEntryLink
from cms.plugins.text.cms_plugins import TextPlugin
from cms.plugins.text.utils import plugin_tags_to_user_html
from django.utils.text import truncate_words
from django.conf import settings

class CMSFaqEntryPlugin(TextPlugin):
    """Subclass of Text plugin, includes 'topic' & 'css' fields"""

    model = FaqEntry
    name = _("FAQ Entry")
    render_template = "plugins/cms/faq_entry.html"

    def render(self, context, instance, placeholder):
        if settings.CMS_DBGETTEXT:
            from dbgettext.parser import parsed_gettext
            instance.topic = parsed_gettext(instance, 'topic')
            instance.body = parsed_gettext(instance, 'body')
        context.update({
            'body':plugin_tags_to_user_html(instance.body, context, placeholder),
            'topic':instance.topic,
            'css' : instance.get_css_display(),
            'placeholder':placeholder,
            'object':instance,
        })
        return context

plugin_pool.register_plugin(CMSFaqEntryPlugin)

class CMSFaqListPlugin(CMSPluginBase):
    """Lists all FaqEntry plugins on the same page as this plugin"""

    model = FaqList
    name = _("FAQ List")
    render_template = "plugins/cms/faq_list.html"

    def render(self, context, instance, placeholder):
        #get all FaqEntryPlugins on this page and in this language
        language = context.get('lang', settings.LANGUAGE_CODE)
        #plugins = instance.page.cmsplugin_set.filter(plugin_type='CMSFaqEntryPlugin', language=language)
        plugins CMSFaqEntryPlugin.objects.filter(language=language)

        faqentry_plugins = []

        #make a list of the faqentry plugin objects
        for plugin in plugins:
            #truncate the entry's body
            if instance.truncate_body:
                plugin.faqentry.body = truncate_words(plugin.faqentry.body, instance.truncate_body)
            #show the entry's body or not
            if not instance.show_body:
                plugin.faqentry.body = ''
            faqentry_plugins.append(plugin.faqentry)

        context.update({
            'faq_list': faqentry_plugins,
            'css': instance.get_css_display(),
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSFaqListPlugin)


class CMSFaqEntryLinkPlugin(CMSPluginBase):
    """Links to a single FaqEntry plugins"""

    model = FaqEntryLink
    name = _("FAQ Entry Link")
    text_enabled = True
    render_template = "plugins/cms/faq_entry_link.html"

    def render(self, context, instance, placeholder):

        #if a faqentry is not specified, choose one at random
        if not instance.link:
            faqentry_plugins = []
            #get all FaqEntryPlugins
            plugins = CMSPlugin.objects.filter(plugin_type='CMSFaqEntryPlugin')
            #make a list of the faqentry plugin objects
            for plugin in plugins:
                faqentry_plugins.append(plugin.faqentry)
            try:
                #choose a random one
                import random
                instance.link = random.sample(faqentry_plugins, 1)[0]
                #set the page id of the linked faqentry
                page_id = instance.link.page_id
            except (ValueError, AttributeError):                    #since this didn't work, we assume no plugin exists
                raise ValueError("No FaqEntryPlugin was returned. Make sure one exists and is published.")

        #truncate the entry's body
        if instance.truncate_body and instance.link.body:
            instance.link.body = truncate_words(instance.link.body, instance.truncate_body)

        #show the entry's body or not
        if not instance.show_body:
            instance.link.body = ''

        #create the link URL
        #if page_id was not set randomly
        try:
            page_id
        except (NameError, UnboundLocalError):
            page_id = instance.faqentrylink.link.page_id
#        import ipdb; ipdb.set_trace()
        #check if multilingual middleware is installed
        if 'cms.middleware.multilingual.MultilingualURLMiddleware' in settings.MIDDLEWARE_CLASSES:
            url = '/' + instance.link.language + Page.objects.get(id=page_id).get_absolute_url(language=instance.link.language)
        else:
            url = Page.objects.get(id=page_id).get_absolute_url()

        context.update({
            'body': plugin_tags_to_user_html(instance.link.body, context, placeholder),
            'topic': instance.link.topic,
            'url': url,
            'css': instance.get_css_display(),
            'placeholder': placeholder,
            'object': instance,
        })
        return context

plugin_pool.register_plugin(CMSFaqEntryLinkPlugin)
