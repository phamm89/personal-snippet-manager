from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from core.models import Snippet, CustomUser, UserPage
from core.forms import SnippetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import SnippetFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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



# View to copy snippet
def copy_snippet(request, pk):
    """View function for user to copy snippet to user page."""
    snippet = get_object_or_404(Snippet, pk=pk)
    
    if request.method == 'GET':
        if request.user in snippet.copy_snippet.all():
            snippet.copy_snippet.remove(request.user)
            messages.info(request, f"You have removed {snippet.copy_snippet} from your user page.")
        else:
            snippet.copy_snippet.add(request.user)
            messages.success(request, f"You have added {snippet.copy_snippet} to your user page.")
            
    return HttpResponseRedirect(request.GET.get("next"))



def user_list(request):
    """View function for user to view all code snippets on user list."""
    user_list = UserPage.objects.filter(user=request.user)

    return render(request, 'core/user_list.html', {'user_list': user_list})

# View to delete snippet
def snippet_delete(request, id=None):
    snippet = Snippet.objects.get(id=id)

    if request.method =="GET":
        snippet.delete()
        messages.success(request, "Code snippet deleted!")
        return redirect('index')

    
    return render(request, 'core/snippet_delete.html')

# View to search snippet
def search_snippet(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    snippets = Snippet.objects.filter(title__contains=search_text)

    return render(request, 'base.html', {'snippets': snippets})


class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = 'core/snippet_delete.html'
    success_url = reverse_lazy('snippets')

    def form_validation(self, request):

        if self.request.is_ajax():
            return JsonResponse({"complete": True})

        return redirect('core/snippet_list.html')


def all_public_snippets(request):
    template_name = 'core/search_list.html'
    snippets = Snippet.objects.filter()
    snippets_filter = SnippetFilter(request.GET, queryset=snippets)

    return render(request, 'core/search_list.html', {'filter': snippets_filter})
    