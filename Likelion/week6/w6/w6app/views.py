from django.shortcuts import render
from .models import Playlist

# Create your views here.
def index(request) :
    songs = Playlist.objects.all()
    return render(request, 'index.html', {'songs':songs})

