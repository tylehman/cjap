from django.conf.urls import url
from django.views.generic import ListView, DetailView
from jobs.models import JobInfo
from find_job.models import FindJob
from views import Detail_Job_Data, Find_a_job
from . import views
from django import forms
from django.utils.translation import ugettext
from filters import JobTitleFilter
from django_filters.views import FilterMixin


import django_filters
from django_filters.filterset import ORDER_BY_FIELD

from views import FilterMixin

class JobListView(FilterMixin, django_filters.views.FilterView):
    paginate_by = 10
    filterset_class = JobTitleFilter
    template_name = 'find_job/find_job.html'
    job_list = JobInfo.objects.all().order_by('-job_posted')

urlpatterns = [
                # url(r'^$', Find_a_job.as_view()),
                url(r'^$', JobListView.as_view(), name="find_job"),
                url(r'^(?P<pk>\d+)$', Detail_Job_Data.as_view(),
                    ),
            ]
