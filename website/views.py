from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProtectedView(TemplateView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProtectedView, self).dispatch(*args, **kwargs)

class HomeView(TemplateView):
	template_name = "pages/home.html"

class PreviewView(TemplateView):
	template_name = "pages/preview.html"

class ProfileView(ProtectedView):
	template_name = "registration/profile.html"
