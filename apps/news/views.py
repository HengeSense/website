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

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404

from apps.news.models import News
from apps.news.settings import NEWS_PER_PAGE, NUMBER_TRUNCATE_WORDS

def listing(request, page=None):
	news_list = News.pubs_objects.all()
	paginator = Paginator(news_list, NEWS_PER_PAGE)

	# Make sure page request is an int. If not, deliver first page.
	if page is None:
		page = 1

	# If page request (9999) is out of range, deliver last page of results.
	try:
		news = paginator.page(page)
	except (EmptyPage, InvalidPage):
		news = paginator.page(paginator.num_pages)

	return render_to_response("news_listing.html",
		{"news": news,
		 "words": NUMBER_TRUNCATE_WORDS},
		context_instance=RequestContext(request))

def listing_tags(request, tag, page=None):
	news_list = News.pubs_objects.filter(tags__name__in=[tag])
	paginator = Paginator(news_list, NEWS_PER_PAGE)

	# Make sure page request is an int. If not, deliver first page.
	if page is None:
		page = 1

	# If page request (9999) is out of range, deliver last page of results.
	try:
		news = paginator.page(page)
	except (EmptyPage, InvalidPage):
		news = paginator.page(paginator.num_pages)

	return render_to_response("news_listing.html",
		{"news": news,
		 "tag": tag,
		 "words": NUMBER_TRUNCATE_WORDS},
		context_instance=RequestContext(request))

def news_details(request, slug=None):
	news = get_object_or_404(News, slug=slug)

	if not news.published:
		raise Http404

	return render_to_response("news_detail.html",
		{"news": news},
		context_instance=RequestContext(request))
