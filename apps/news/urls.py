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

from django.conf.urls.defaults import *

from apps.news.feeds import RssLatestNewsFeed, AtomLatestNewsFeed

urlpatterns = patterns('apps.news.views',
	url(r'^$', 'listing', name='list_news'),
	url(r'^tags/(?P<tag>[\w-]+)/$', 'listing_tags', name='news_tags'),
	url(r'^tags/(?P<tag>[\w-]+)/(?P<page>\d+)/$', 'listing_tags', name='news_tags'),
	url(r'^(?P<page>\d+)/$', 'listing', name='list_news'),
	url(r'^(?P<slug>[\w-]+)/$', 'news_details', name='news_details'),
)

urlpatterns += patterns('',
	# RSS
	(r'feeds/rss/$', RssLatestNewsFeed()),
	(r'feeds/atom/$', AtomLatestNewsFeed())
)
