# courses/context_processors.py

from .models import SchoolLevel

def all_levels(request):
    return {
        'all_levels': SchoolLevel.objects.all()
    }