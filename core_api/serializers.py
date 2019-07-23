from core.models import CustomUser, Snippet
from rest_framework import serializers

# Serializers Created Here
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class SnippetSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True)

    PYTHON = 'python'
    JAVASCRIPT = 'js'
    HTML = 'html'
    LUA = 'lua'
    CSS = 'css'
    CLIKE = 'clike'
    MARKUP = 'markup'
    HTML = 'html'
    BASH = 'bash'
    DJANGO ='django'
    GO = 'go'
    JSON = 'json'
    HTTP = 'http'
    PHP = 'php'
    RUBY = 'ruby'
    SAS = 'sas'
    SASS = 'sass'
    SCSS = 'scss'
    SQL = 'sql'

    LANGUAGE_CHOICES = [
    (PYTHON, 'python'),
    (JAVASCRIPT, 'js'),
    (HTML, 'html'),
    (LUA, 'lua'),
    (CSS, 'css'),
    (CLIKE, 'clike'),
    (MARKUP, 'markup'),
    (HTML, 'html'),
    (BASH, 'bash'),
    (DJANGO, 'django'),
    (GO, 'go'),
    (JSON, 'json'),
    (HTTP, 'http'),
    (PHP, 'php'),
    (RUBY, 'ruby'),
    (SAS, 'sas'),
    (SASS, 'sass'),
    (SCSS, 'scss'),
    (SQL, 'sql'),
    ]
    languages = serializers.CharField(max_length=7,choices=LANGUAGE_CHOICES,default=HTML,)
    code = serializers.TextField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    description = serializers.TextField(max_length=200, null=True, allow_blank=True)
    creator = serializers.ForeignKey(to=CustomUser)
    date_added = serializers.DateTimeField(auto_now_add=True)


    class Meta:
        model = Snippet
        fields = ['title', 'languages', 'code', 'description', 'creator', 'date_added', 'pk']