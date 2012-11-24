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

from django.views.generic import TemplateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from website.forms import EditProfileForm

class ProtectedView(TemplateView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProtectedView, self).dispatch(*args, **kwargs)

class ProtectedFormView(FormView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProtectedFormView, self).dispatch(*args, **kwargs)

class HomeView(TemplateView):
	template_name = "pages/home.html"

class PreviewView(TemplateView):
	template_name = "pages/preview.html"

class ProfileView(ProtectedView):
	template_name = "registration/profile.html"

class EditProfileView(ProtectedFormView):
	template_name = "registration/profile.html"
	http_method_names = ["get", "post"]
	form_class = EditProfileForm
	success_url = reverse_lazy("auth_profile")

	def get_context_data(self, **kwargs):
		context = super(EditProfileView, self).get_context_data(**kwargs)
		context["edit_mode"] = True
		return context

	def get_initial(self):
		return {
			"first_name": self.request.user.first_name,
			"last_name": self.request.user.last_name,
			"date_of_birth": self.request.user.get_profile().date_of_birth,
			"gender": self.request.user.get_profile().gender,
			"receive_updates": self.request.user.get_profile().receive_updates
		}

	def post(self, request, *args, **kwargs):
		# Make sure the user is authenticated
		if not request.user.is_authenticated():
			from django.http import HttpResponseForbidden
			return HttpResponseForbidden()

		# Form
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		form.request = request

		if form.is_valid():
			cleaned_data = form.clean()
			request.user.first_name = cleaned_data["first_name"]
			request.user.last_name = cleaned_data["last_name"]
			request.user.get_profile().date_of_birth = cleaned_data["date_of_birth"]
			request.user.get_profile().gender = cleaned_data["gender"]
			request.user.get_profile().receive_updates = cleaned_data["receive_updates"]
			request.user.save()
			request.user.get_profile().save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
