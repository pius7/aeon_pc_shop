# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages, auth

# Create your views here.

def view_account(request):

    """A view that displays the index page"""
    return render(request, "view_accounts.html")
    
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return render(request, "home/index.html")
    
def register(request):
    
    return render(request, "register.html")
    
def login(request):
    
    return render(request, "login.html")