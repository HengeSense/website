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
