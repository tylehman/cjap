from jobs.models import JobInfo
from find_job.models import FindJob
import django_filters

class JobTitleFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains', label='Job Title')
    comp_name = django_filters.CharFilter(lookup_expr='icontains', label='Company Name')
    job_addr = django_filters.CharFilter(lookup_expr='icontains', label='Company Location')
    job_link = django_filters.CharFilter(lookup_expr='icontains', label='Additional Search Info')
    job_posted = django_filters.DateFilter(name='job_posted', label='Date Posted')

    class Meta:
        model = JobInfo
        fields = ['job_title', 'comp_name', 'job_addr', 'job_link', 'job_posted',]
