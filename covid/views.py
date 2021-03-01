#Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


def hi(request):
    """Return a greeting."""
    now = datetime.now().strftime(' %b %dth, %y - %H:%M hrs')
    return HttpResponse('Hi! Current server time is{now}'.format(now=now))
