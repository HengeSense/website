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

		node = NavigationNode(_("Index"), "/news", 0)
		nodes.append(node)

		for item in News.pubs_objects.all()[:10]:
			node = NavigationNode(
				item.title,
#				reverse("news_details", kwargs={"slug": item.slug}),
				"/news/%s" % item.slug,
				item.pk
			)
			nodes.append(node)
		return nodes
menu_pool.register_menu(NewsMenu)
