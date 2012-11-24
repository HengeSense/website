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

from django.contrib import admin

from apps.news.models import Category, News
from apps.news.forms import NewsAdminModelForm

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)
admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title", "category", "user", "created_at", "published", "comments_enabled")
	search_fields = ["body", "title", "category"]
	ordering = ("-created_at",)
	list_filter = ("created_at", "updated_at", "published", "comments_enabled")
	
	fieldsets = [
		("General", {"fields": ["user", "site", "title", "slug"],}),
		("", {"fields": ["category", "body", "tags"]}),
		("Publishing", {"fields": ["published", "comments_enabled"]}),
	]
	form = NewsAdminModelForm
admin.site.register(News, NewsAdmin)
