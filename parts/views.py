# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def show_parts(request):

    """A view that displays the index page"""
    return render(request, "products.html")