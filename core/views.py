from django.shortcuts import render, get_list_or_404, redirect
from core.models import Snippet
from core.forms import SnippetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import SnippetFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic


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

# View to update snippet
class SnippetUpdate(UpdateView):
    """View for editing daily record"""
    model = Snippet
    fields = '__all__'
    success_url = reverse_lazy('index')

class SnippetListView(generic.ListView):
    model = Snippet

class SnippetDetailView(generic.DetailView):
    model = Snippet

# View to delete snippet
def delete_snippet(request, pk):
    snippet = Snippet.objects.get(pk=id)

    if request.method =="POST":
        snippet.delete()
        messages.success(request, "Code snippet deleted!")
        return redirect('index')

    
    return render(request, 'core/snippet_confirm_delete.html')

# View to search snippet
def search_snippet(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    snippets = Snippet.objects.filter(title__contains=search_text)

    return render(request, 'base.html', {'snippets': snippets})

class SnippetDelete(DeleteView):
    model = Snippet
    success_url = reverse_lazy('index')
    