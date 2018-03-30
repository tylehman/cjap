# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib.auth.decorators import login_required

def contact(request):
    return render(request, 'about/contact.html')

