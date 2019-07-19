from django.shortcuts import render
from core.models import Snippet

# Views created for Code Snippet
def index(request):
    """View function for home page of site."""

    snippet_codes_count = Snippet.objects.all().count()
    snippet_codes = Snippet.objects.all()

    context = {
        'snippet_codes_count': snippet_codes_count,
        'snippet_codes': snippet_codes
    }

    return render(request, 'index.html', context=context)