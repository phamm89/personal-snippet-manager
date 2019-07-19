from django.shortcuts import render, get_list_or_404, redirect
from core.models import Snippet
from core.forms import SnippetForm
from django.views.generic.edit import CreateView

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

# Method for adding a snippet
def add_snippet(request):
    snippet = get_list_or_404(Snippet)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.post = Snippet
            form.save(Snippet)
            return redirect('index')
    else:
        form = SnippetForm()
    return render(request, 'core/snippet_form.html', {'form':form})
