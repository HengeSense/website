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

from django.conf import settings

#### Default number of news per page
NEWS_PER_PAGE = getattr(settings, "NEWS_PER_PAGE", 4)

#### Number of truncate words in news
NUMBER_TRUNCATE_WORDS = getattr(settings, "NUMBER_TRUNCATE_WORDS", '40')

#### Configuration for feeds
FEED_TITLE =  getattr(settings, "FEED_TITLE", "News sample application")
FEED_LINK = getattr(settings, "FEED_LINK", "news/")
FEED_DESCRIPTION = getattr(settings, "FEED_DESCRIPTION", "Updates on changes and additions to sample application.")
FEED_COUNT = getattr(settings, "FEED_COUNT", 5)

#### News media path 
NEWS_MEDIA_URL = getattr(settings, "NEWS_MEDIA_URL", "/media/news/")
