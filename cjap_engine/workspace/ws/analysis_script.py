import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import itertools
import os

df = pd.read_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/master.csv', encoding='utf-8',
                 index_col=0)


def job_type_counter():
    job_type_num = df.groupby('job_type').count()
    return job_type_num


def top_job_type_sort():
    jt_df = job_type_counter()
    jt_df = jt_df.sort_values('job_title', ascending=True)
    return jt_df['job_title'].ix[19:]


def job_type_db_query():
    job_type_db = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/job_type.db"
    conn = sqlite3.connect(job_type_db)
    c = conn.cursor()
    job_list = []
    for index, row in top_job_type_sort().iteritems():
        ind = str(index)
        c.execute("SELECT DISTINCT job_title FROM job_type_data WHERE job_category='{top_job}'".format(top_job=ind))
        all_rows = c.fetchall()
        for n in all_rows:
            job_type = zip(itertools.repeat(ind), n)
            job_list.append(job_type)
    return job_list


def job_suggestions_db():
    appended_data = []
    for n in job_type_db_query():
        dfn = pd.DataFrame.from_records(n)
        appended_data.append(dfn)
    appended_data = pd.concat(appended_data, axis=0)
    return appended_data
    # df = appended_data.ix[:, 3] = "(`" + appended_data.ix[:, 0].map(str) + "`,`" + appended_data.ix[:, 1].map(str) + "`),"
    return df

# print job_suggestions_db(), type(job_suggestions_db())


def db_creator():
        job_type_db = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/job_suggs.db"
        try:
            os.remove(job_type_db)
        except:
            pass
        # this returns the sorted amount of jobs per job_type
        conn = sqlite3.connect(job_type_db)
        c = conn.cursor()
        c.execute('CREATE TABLE job_suggs'
                                   '(job_category CHAR(50), job_title CHAR(50))')
        for index, row in job_suggestions_db().iterrows():
            c.execute('INSERT INTO job_suggs VALUES (?,?)', (row[0], row[1]))

        conn.commit()
        return conn.commit()

db_creator()

# print job_type_sort_graph(), type(job_type_sort_graph())
# this graphs the 10 highest job count but in reverse
def top_job_type_graph():
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use('fivethirtyeight')
    ax = top_job_type_sort().plot.barh()
    ax.set_ylabel('Job Category')
    plt.savefig('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/job_type_graph.png')
    return ax


# this is what returns the graph
top_job_type_graph()
plt.show()
plt.close()

# returns counts of job postings per day and returns job postings over the past week
def jobs_posted_today():
    jobs_just_posted = df.groupby('job_posted').count()
    return jobs_just_posted['job_title'].ix[(-7):]


# graph job count per day
def job_post_numbers_graph():
    plt.title('Number of Jobs per Day')
    plt.xlabel('Date')
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use('ggplot')
    ax = jobs_posted_today().plot.bar()
    ax.set_ylabel('Jpb Count')
    ax.set_xlabel('')
    plt.savefig('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/job_count_graph.png')
    return ax


# this is what returns the graph
job_post_numbers_graph()
plt.show()
