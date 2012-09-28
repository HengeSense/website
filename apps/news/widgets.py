from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class TinyMCEEditor(forms.Textarea):
	class Media:
		js = (
			"js/jquery-1.8.1.min.js",
			"js/jquery.tinymce.js",
		)

	def __init__(self, language=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		super(TinyMCEEditor, self).__init__()

	def render(self, name, value, attrs=None):
		rendered = super(TinyMCEEditor, self).render(name, value, attrs)
		context = {
			"name": name,
			"lang": self.language[:2],
			"language": self.language,
			"STATIC_URL": settings.STATIC_URL,
		}

		return rendered + mark_safe(render_to_string(
			"admin/news/widgets/tinymce.html", context))

class WYMEditor(forms.Textarea):
	class Media:
		js = (
			"js/jquery-1.8.1.min.js",
			"cms/wymeditor/jquery.wymeditor.pack.js",
		)

	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {"class": "wymeditor"}
		if attrs:
			self.attrs.update(attrs)
		super(WYMEditor, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(WYMEditor, self).render(name, value, attrs)
		context = {
			"name": name,
			"lang": self.language[:2],
			"language": self.language,
			"STATIC_URL": settings.STATIC_URL,
			"page_link_wymeditor": 0,
			"filebrowser": 0,
		}

		return rendered + mark_safe(render_to_string(
			"admin/news/widgets/wymeditor.html", context))
