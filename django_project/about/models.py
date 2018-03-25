# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

now = timezone.now()
class UserDB(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30, blank=False, null=False)
    user_phone = models.CharField(max_length=30, blank=False, null=False)
    date_signed_up = models.DateTimeField(default=timezone.now)

    def sign_up(self):
        self.date_signed_up = now
        self.save()

    def __unicode__(self):
        return self.user_email
