from django.conf.urls import patterns, include, url
from django.conf import settings
from cms.sitemaps import CMSSitemap

from django.contrib import admin
admin.autodiscover()

from website.views import HomeView, PreviewView, ProfileView, EditProfileView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home_page"),
    url(r'^preview/$', PreviewView.as_view(), name="preview_page"),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap
        }
    }),
    url(r'^accounts/profile/edit/$', EditProfileView.as_view(), name="auth_edit_profile"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="auth_profile"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler500 = "mauiwebsite.core.views.server_error"
