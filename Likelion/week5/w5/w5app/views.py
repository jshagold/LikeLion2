# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def about(request) :
    return render(request, 'about.html')

def result(request) :
    full_text = request.GET['fulltext']
    return render(request, 'result.html')