import pandas as pd
import sqlite3
import ast
import re
import os
import string
from dateutil import parser

# Read in the Dataset
inf = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data.csv"
df = pd.DataFrame()
df = pd.read_csv(inf, header=None, index_col=None)
df = df.drop(df.index[0])

# Convert the string date time col, job-posted, to a date format
# job_posted = df.iloc[:,4]
# for index, row in df.iterrows():
#     jp = parser.parse(row.iloc[4])
# df.iloc[:,4] = jp

print df
try:
    os.remove('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/jobs.db')
except:
    pass
conn = sqlite3.connect('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/jobs.db')
c = conn.cursor()

c.execute(""" CREATE TABLE job_info
        ( id INTEGER PRIMARY KEY, job_title CHAR(50), comp_name CHAR(50), job_addr CHAR(50), job_link CHAR(50),
            job_posted CHAR(50), job_search CHAR(50)
        )
""")

# Concatenate Columns into 1 string
df.ix[:, 10] = "(`" \
                  + df.ix[:, 0].map(str) \
                  + "`,`" \
                  + df.ix[:, 6].map(str) \
                  + "`,`" \
                  + df.ix[:, 1].map(str) \
                  + "`,`" \
                  + df.ix[:, 2].map(str) \
                  + "`,`" \
                  + df.ix[:, 3].map(str) \
                  + "`,`" \
                  + df.ix[:, 4].map(str) \
                  + "`,`" \
                  + df.ix[:, 5].map(str) \
                  + "`),"

testData = df.ix[:, 10]
printable = set(string.printable)
filter(lambda w: w in printable, testData)
for x in testData:
    reg1 = re.compile(r'[`]+')
    reg2 = re.compile(r"['\*]*")
    b = re.sub(reg2, "", x)
    d = re.sub(reg1, "'", b)

    try:
        d = ast.literal_eval(d)
    except SyntaxError:
        pass
    try:
        c.executemany('INSERT INTO job_info VALUES (?,?,?,?,?,?,?)', d)
    except sqlite3.ProgrammingError:
        pass

for row in c.execute('SELECT * FROM job_info'):
    print "row = ",row

conn.commit()