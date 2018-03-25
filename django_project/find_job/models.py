# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jobs.models import JobInfo

class FindJob(JobInfo):
    today = models.DateField()
