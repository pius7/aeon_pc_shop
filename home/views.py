# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):

    """A view that displays the index page"""
    return render(request, "home/index.html")
    
def about(request):

    """A view that displays the index page"""
    return render(request, "home/about.html")
    

    

