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
