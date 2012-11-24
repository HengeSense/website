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

from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "gender", "receive_updates")
	list_filter = ("gender", "receive_updates")
	list_select_related = True
	ordering = ("date_of_birth",)
	search_field = ["user__username", "user__fist_name", "user__last_name", "user__email"]
	fieldsets = (
		(None, {
			"fields": ("user",)
		}),
		(_("Profile"), {
			"fields": ("date_of_birth", "gender", "receive_updates")
		})
	)
admin.site.register(UserProfile, UserProfileAdmin)
