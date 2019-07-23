from django.urls import path
from core_api import views as core_api_views


urlpatterns = [
   path("snippets/", core_api_views.SnippetListCreateView.as_view(),
        name="api_snippets_list"),
    path("user_snippets/", core_api_views.CustomUserListCreateView.as_view(),
         name="user_snippets_list"),
   path(
       "snippets/<pk>/",
       core_api_views.SnippetRetrieveUpdateDestroyView.as_view(),
       name="api_snippet"),
   path("users/", core_api_views.UserListView.as_view(), name="api_users_list"),

]