############################################################################
# This file is part of the Maui Web site.
#
# Copyright (c) 2012 Pier Luigi Fiorini
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

from apps.news.models import News

def get_editor_widget():
	from django.conf import settings
	from cms.plugins.text.settings import USE_TINYMCE
	if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
		from apps.news.widgets import TinyMCEEditor
		return TinyMCEEditor()
	else:
		from apps.news.widgets import WYMEditor
		return WYMEditor()

class NewsAdminModelForm(forms.ModelForm):
	body = forms.CharField(widget=get_editor_widget())

	class Meta:
		model = News
