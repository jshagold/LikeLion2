from .models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        # fields = '__all__'
        fields = ['title', 'body', 'user']