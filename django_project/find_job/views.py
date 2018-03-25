# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from jobs.models import JobInfo
from find_job.models import FindJob
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from filters import JobTitleFilter
from django_filters import views as filters_views
import django_filters
from django_filters.views import FilterMixin


class FilterMixin(filters_views.FilterMixin):

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super(FilterMixin, self).get_filterset_kwargs(filterset_class)
        if kwargs['data'] is not None and 'page' in kwargs['data']:
            data = kwargs['data'].copy() ; del data['page']
            kwargs['data'] = data
        return kwargs

class Find_a_job(FilterMixin, django_filters.views.FilterView):

    model = JobInfo
    paginate_by = 10
    job_list = JobInfo.objects.all().order_by('-job_posted')
    template_name = 'find_job/find_job.html'
    context_object_name = 'job'
    paginator = Paginator(job_list, 10)
    job_filter = JobTitleFilter
    filterset_class = JobTitleFilter
    job_title_filter = job_filter(queryset=job_list)

# This works
    #
    def get(self, request, *args, **kwargs):
        job_title_filter = self.filterset_class(request.GET, queryset=self.job_list)
        return render(request, self.template_name, {'filter' : job_title_filter})

# This isn't working
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=JobInfo.objects.all())
    #     return super(Find_a_job, self).get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(Find_a_job, self).get_context_data(**kwargs)
    #     context[{'filter' : job_title_filter}] = self.object
    #     return context
    #
    # def get_queryset(self):
    #     return self.object.job_list.all()

class Detail_Job_Data(DetailView):
    model = JobInfo
    template_name = "find_job/each_job_info.html"
