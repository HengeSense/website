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

from django.test import TestCase
from django.test.client import Client

class NewsEmptyTestCase(TestCase):
	def test_01_empty_news(self):
		c = Client()

		response = c.get('/news/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('No news so far' in response.content)

		response = c.get('/news/1', follow=True)
		self.assertEqual(response.status_code, 200)

class NewsTestCase(TestCase):
	fixtures = ['test_auth.json', 'test_news.json']

	def test_01_news(self):
		c = Client()

		response = c.get('/news/', follow=True)
		self.assertEqual(response.status_code, 200)

		response = c.get('/news/1/', follow=True)
		self.assertEqual(response.status_code, 200)

		response = c.get('/news/2/', follow=True)
		self.assertEqual(response.status_code, 200)

		response = c.get('/news/?page=3000', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('<a href="/news/2/">2</a>' in response.content)

	def test_02_news(self):
		c = Client()

		response = c.get('/news/lorem-ipsum-dolor-sit-amet/1/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('<a href="/news/1/">' in response.content)

		response = c.get('/news/2/', follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('<h4><a href="/news/cum-sociis-natoque-penatibus-e/2/">Cum sociis natoque penatibus e</a></h4>' in response.content)

class FeedsTestCase(TestCase):
	fixtures = ['test_auth.json', 'test_news.json']

	def test_01_feeds(self):
		c = Client()

		response = c.get('/news/feeds/rss/', follow=True)
		self.assertEqual(response.status_code, 200)
