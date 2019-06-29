from django.shortcuts import render
from .models import Members

# Create your views here.
def index(request) :
    members = Members.objects.filter(nationality = '일본')
    return render(request, 'index.html', {'japanese' : members})
