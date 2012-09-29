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
		("Publishing", {"fields": ["published", "comments_enabled", "created_at", "updated_at"]}),
	]
	form = NewsAdminModelForm
admin.site.register(News, NewsAdmin)
