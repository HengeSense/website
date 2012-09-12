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
