# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20170527_1636'),
        ('find_job', '0002_auto_20171121_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindJob',
            fields=[
                ('jobinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='jobs.JobInfo')),
                ('today', models.DateField()),
            ],
            bases=('jobs.jobinfo',),
        ),
    ]
