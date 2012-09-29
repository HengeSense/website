from django import forms

class EditProfileForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	date_of_birth = forms.DateField()
	gender = forms.CharField()
	receive_updates = forms.BooleanField(required=False)
