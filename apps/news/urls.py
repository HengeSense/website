from django.conf.urls.defaults import *

from apps.news.feeds import RssLatestNewsFeed, AtomLatestNewsFeed

urlpatterns = patterns('apps.news.views',
	url(r'^$', 'listing', name='list-news'),
	url(r'^tags/(?P<tag>[\w-]+)/$', 'listing_tags', name='news_tags'),
	url(r'^tags/(?P<tag>[\w-]+)/(?P<page>\d+)/$', 'listing_tags', name='news_tags'),
#	url(r'^(?P<page>\d+)/$', 'listing', name='list-news'),
	url(r'^(?P<slug>[\w-]+)/$', 'news_details', name='news-details'),
)

urlpatterns += patterns('',
	# RSS
	(r'feeds/rss/$', RssLatestNewsFeed()),
	(r'feeds/atom/$', AtomLatestNewsFeed())
)
