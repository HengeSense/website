from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from apps.news.menu import NewsMenu

class NewsApp(CMSApp):
	name = _("News App")
	urls = ["apps.news.urls"]
	menus = [NewsMenu]

apphook_pool.register(NewsApp)
