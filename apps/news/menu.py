from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from apps.news.models import News

class NewsMenu(CMSAttachMenu):
	name = _("News Menu")

	def get_nodes(self, request):
		nodes = []
		for item in News.pubs_objects.all():
			node = NavigationNode(
				item.title,
#				reverse("news_details", kwargs={"slug": item.slug}),
				"/news/%s" % item.slug,
				item.pk
			)
			nodes.append(node)
		return nodes
menu_pool.register_menu(NewsMenu)
