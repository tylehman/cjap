import pandas as pd
import re


class job_obj():
    df = pd.DataFrame({'Neo': [1,2,3], 'words': ['i hope this works', 'tester', 'spongebob under a pineapple']})
    
lookups = [
    (r'(wor)', '1 UP'),
    (r'(pin)', 'AYEAYE'),
]


def lookup(s, lookuplist):
    for pattern, value in lookuplist:
        if re.search(pattern, s):
            return value
    return 'nonono'


df_job_obj = job_obj.df
word_series = job_obj.df['words']
df1 = pd.DataFrame()

def df_scanner(ser, df):
    for ind, val in ser.iteritems():
        ahHa = lookup(val, lookups)
        df = df.append({'job_type': ahHa}, ignore_index=True)
    return df
    
job_type_series = df_scanner(word_series, df1)

df_new = pd.concat([df_job_obj, job_type_series], axis=1, ignore_index=True)

print df_new