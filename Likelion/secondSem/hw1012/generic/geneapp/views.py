from django.shortcuts import render
from geneapp.models import Snippet
from geneapp.serializer import SnippetSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
