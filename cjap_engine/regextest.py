# load the library
import pandas as pd
import urllib
import re

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup as Soup  #  For HTML Parsing

import time
import datetime

start = time.time()
print "start = ", datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

pd.set_option('max_colwidth', 500)  # remove column limits or info will be lost
df = pd.DataFrame()  # Create a new data frame

df = pd.read_csv('/Users/tylehman/Desktop/connectCO.csv')
df = df.replace({r' - ': '', r'(\[)': '', r']': ''}, regex=True)
df['job_title'] = df['job_posted'].replace({r'^ [a-zA-Z ]*': ''}, regex=True)
df = df[df.job_title != '']


print df['job_title']
df.to_csv('/Users/tylehman/Desktop/connectCOregex.csv', encoding='utf-8')

end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
