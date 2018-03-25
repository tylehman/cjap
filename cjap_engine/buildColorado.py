# load the library
import pandas as pd
import urllib
import re

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup as Soup  #  For HTML Parsing

import time
import datetime

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

start = time.time()
print "start = ", datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

pd.set_option('max_colwidth', 500)  # remove column limits or info will be lost
df = pd.DataFrame()  # Create a new data frame

base_url = 'http://agc-co.ourcareerpages.com/CareerPage.aspx?ccpcode=agc-co'
driver = webdriver.Firefox(capabilities=caps)
driver.get(base_url)

line = driver.find_elements_by_xpath('//div[@class="jobSection"]')
for li in line:
    comp_name = "Build Colorado"
    try:
        job = li.text
        job_title = re.findall('^.* - *', job)
        job_addr = re.findall('^.* - ([a-zA-Z ]*)', job)
    except AttributeError:
        job_title = "null"
    try:
        job_link = li.find_element_by_tag_name("a").get_attribute("href")
    except AttributeError:
        job_link = "null"
    job_posted = "null"
    job_srch = "Construction"
    df = df.append({'comp_name': comp_name,
                      'job_title': job_title,
                      'job_link': job_link,
                      'job_addr': job_addr,
                      'job_posted': job_posted,
                      'job_srch': job_srch
                            }, ignore_index=True)

#df['job_title'] = df['job_title'].replace({r' - ]': '', r'(\[)': '' }, regex=True)
df.to_csv('/Users/tylehman/Desktop/python/sqlite/test.csv', encoding='utf-8')

df = pd.read_csv('/Users/tylehman/Desktop/python/sqlite/test.csv')
df['job_title'] = df['job_title'].replace({r' - ]': '', r'(\[)': '' }, regex=True)
#df['job_title'] = df['job_title'].replace({r'(\[)': ''}, regex=True)

print df['job_title']
df.to_csv('/Users/tylehman/Desktop/python/sqlite/testRegex.csv', encoding='utf-8')
end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
