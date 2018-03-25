# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo

class JobsTemplate(ListView):
    model = JobInfo
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 100
    queryset = JobInfo.objects.all()

class EachJobTemplate(DetailView):
    model = JobInfo
    template_name = "jobs/jobinfo.html"
