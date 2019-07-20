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
        fields = ['title', 'languages', 'snippet_code', 'description', 'creator', 'copy', 'date_added', 'pk']