from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "gender")
	list_select_related = True
	ordering = ("date_of_birth",)
	search_field = ["user__username", "user__fist_name", "user__last_name", "user__email"]
	fieldsets = (
		(None, {
			"fields": ("user",)
		}),
		(_("Profile"), {
			"fields": ("date_of_birth", "gender")
		})
	)
admin.site.register(UserProfile, UserProfileAdmin)
