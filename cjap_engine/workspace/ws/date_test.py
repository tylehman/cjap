import pandas as pd
from dateutil import parser
from dateutil.relativedelta import *
import datetime


inf = "/Users/tylehman/Desktop/Job Analytics/formated_date.csv"
df = pd.DataFrame()
df = pd.read_csv(inf, header=None, index_col=None)
TODAY = datetime.date.today()
df = df.drop(df.index[0])

job_posted = df.iloc[:,4]
for index, row in df.iterrows():
    jp = parser.parse(row.iloc[4])
df.iloc[:,4] = jp

print df


