from django.shortcuts import render
from core.models import CustomUser, Snippet
from core_api.serializers import CustomUserSerializer, SnippetSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


# Views for API Created Here
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows custom user to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """
    queryset = Snippet.objects.all().order_by('-date_added')
    serializer_class = SnippetSerializer


#View for API to Delete Snippet
class SnippetDelete(generics.DestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetListCreateView(generics.ListCreateAPIView):
    """API endpoint that allows snippets to be listed, created, and searched."""
    serializer_class = SnippetSerializer
    filter_backends = (DjangoFilterBackend,)
    queryset: Snippet.objects.all().order_by("-date_added")

    def get_queryset(self):
        vector = SearchVector('creator', 'languages', 'code',
                              'title', )
        if self.request.GET.get("search"):
            query = self.request.GET.get("search")
            return Snippet.objects.annotate(search=vector).filter(search=query)
        else:
            return Snippet.objects.filter()

    def perform_create(self, serializer):
       print(self.request)
       serializer.save(creator=self.request.user)


class CustomUserListCreateView(generics.ListCreateAPIView):
    """API endpoint that allows user to see snippets for their user page."""
    serializer_class = SnippetSerializer

    def get_queryset(self):
       return self.request.user.snippets

    def perform_create(self, serializer):
       print(self.request)
       serializer.save(creator=self.request.user)

        
