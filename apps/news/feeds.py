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

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

from apps.news.models import News
from apps.news.settings import FEED_TITLE, FEED_LINK, FEED_DESCRIPTION, FEED_COUNT

class RssLatestNewsFeed(Feed):
	feed_type = Rss201rev2Feed
	title = FEED_TITLE
	link = FEED_LINK
	description = FEED_DESCRIPTION

	def items(self):
		return News.pubs_objects.all()[:FEED_COUNT]

class AtomLatestNewsFeed(RssLatestNewsFeed):
	feed_type = Atom1Feed
	subtitle = RssLatestNewsFeed.description

