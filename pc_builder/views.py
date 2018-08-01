# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def start_builder(request):

    """A view that displays the index page"""
    return render(request, "builder.html")


def select_parts(request):
    
    return render(request, "builder".html)