from core.models import CustomUser, Snippet
from rest_framework import serializers

# Serializers Created Here
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['snippet_title', 'snippet_lang', 'snippet_code', 'snippet_description', 'snippet_creator', 'snippet_copy', 'date_added', 'pk']