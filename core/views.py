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

from django.conf import settings
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseServerError

def server_error(request, template_name='500.html'):
    """
    Mimics Django's error handler but adds ``STATIC_URL`` to the
    context.
    """
    context = RequestContext(request, {"STATIC_URL": settings.STATIC_URL})
    t = get_template(template_name)
    return HttpResponseServerError(t.render(context))
