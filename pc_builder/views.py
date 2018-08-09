# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from parts.models import part
import operator

# Create your views here.

def start_builder(request):

    """A view that displays the index page"""
    return render(request, "builder.html")


def select_parts(request):
    all_products=part.objects.filter(category="Gehäuse")
    par=[]
    for i,prod in enumerate(all_products):
        par.append(part.objects.filter(product=prod.id))
    print(par)
    return render(request, "parts.html")
    #{'products': pages}
def compare_item(request):

    return render(request, "compare.html")
    
    
def configurations(request):

    """A view that displays the index page"""
    return render(request, "configurations.html")