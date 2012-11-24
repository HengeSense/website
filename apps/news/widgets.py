############################################################################
# This file is part of the Maui Web site.
#
# Copyright (c) 2012 Pier Luigi Fiorini
# Copyright (c) 2009-2010 Krzysztof Grodzicki
#
# Author(s):
#    Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>
#
# $BEGIN_LICENSE:AGPL3+$
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# $END_LICENSE$
############################################################################

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
