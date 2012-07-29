from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import SubtitleRichTextPage

admin.site.register(SubtitleRichTextPage, PageAdmin)
