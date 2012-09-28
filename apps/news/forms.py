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
