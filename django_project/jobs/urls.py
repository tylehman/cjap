from django.conf.urls import url
from jobs.views import JobsTemplate, EachJobTemplate

urlpatterns = [
                url(r'^$', JobsTemplate.as_view(), name="all_jobs"
                    ),
                url(r'^(?P<pk>\d+)$', EachJobTemplate.as_view(), name="one_job"
                    ),
            ]
