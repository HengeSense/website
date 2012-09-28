from django import forms

from apps.news.models import News
from apps.news.widgets import WYMEditor

class NewsAdminModelForm(forms.ModelForm):
	body = forms.CharField(widget=WYMEditor())

	class Meta:
		model = News
