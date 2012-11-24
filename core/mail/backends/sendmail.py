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

"""
Email backend that uses sendmail as an external process.
"""

import threading

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from subprocess import Popen, PIPE

class EmailBackend(BaseEmailBackend):
	def __init__(self, fail_silently=False, **kwargs):
		super(EmailBackend, self).__init__(fail_silently=fail_silently)
		self._lock = threading.RLock()

	def open(self):
		return True

	def close(self):
		pass

	def send_messages(self, email_messages):
		"""
		Sends one or more EmailMessage objects and returns the number of email
		messages sent.
		"""
		if not email_messages:
			return
		self._lock.acquire()
		try:
			num_sent = 0
			for message in email_messages:
				sent = self._send(message)
				if sent:
					num_sent += 1
		finally:
			self._lock.release()
		return num_sent

	def _send(self, email_message):
		"""A helper method that does the actual sending."""
		if not email_message.recipients():
			return False
		try:
			ps = Popen(["sendmail"] + list(email_message.recipients()), \
				stdin=PIPE)
			ps.stdin.write(email_message.message().as_string())
			ps.stdin.flush()
			ps.stdin.close()
			return not ps.wait()
		except:
			if not self.fail_silently:
				raise
			return False
		return True
