#!/bin/bash

SCRAPER="***DATA HAS BEEN PULLED***"
CLEANER="***DATA HAS BEEN CLEAN***"
SQLED="***DATA HAS BEEN SQLED***"
UPDATED="***VM DB DATA HAS BEEN UPDATED***"
ARCHIVED="***DATA HAS BEEN ARCHIVED***"
BUCKETED="***JOB ALGORITHM RUN***"
ANALYZED="***CALCULATED AND GRAPHED METRICS"

# pull job data
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/workspace/ws/last_leg.py
echo $SCRAPER

# format data
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/workspace/ws/data_format_sql_update.py
echo $CLEANER

# write data to db
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/sqlite_script.py
echo $SQLED

# write data to a csv file for analysis
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/workspace/ws/data_set_agg.py
echo $ARCHIVED

# copy db file to vm
scp /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/jobs.db root@159.89.130.137:/home/django/django_project
echo $UPDATED

# run job algorithm on on formatted data
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/workspace/ws/algo_job_type_script.py
echo $BUCKETED

# Analyze job data, graph data, update model and static files
python /Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/workspace/ws/analysis_script.py
echo $ANALYZED