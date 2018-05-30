from __future__ import unicode_literals
from django.contrib import admin
from . import models
from jobs.models import JobInfo

admin.site.register(models.JobInfo)
