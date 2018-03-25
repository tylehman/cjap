# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'about/home.html')

def contact(request):
    return render(request, 'about/basic.html')

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})

@login_required
def home(request):
    return render(request, 'about/home.html')
