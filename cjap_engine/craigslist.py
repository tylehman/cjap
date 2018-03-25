import pandas as pd
import urllib
import re
from bs4 import BeautifulSoup as Soup  #  For HTML Parsing
import time
import datetime
import utils
start = time.time()
print "start = ", datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

pd.set_option('max_colwidth', 500)  # remove column limits or info will be lost
df = pd.DataFrame()  # Create a new data frame


base_url = ['https://fortcollins.craigslist.org/search/jjj?s=',
            'https://denver.craigslist.org/search/jjj?s=',
            'https://boulder.craigslist.org/search/jjj?s='
            ]

page = [0, 120, 240, 360]

for b in page:
    for a in base_url:
        url = "%s%d" % (a, b)
        target = Soup(urllib.urlopen(url), "lxml")
        targetElements = target.findAll('li', attrs={'class': 'result-row'})

        for elem in targetElements:
            comp_name = "Craigs List"
            try:
                job_title = elem.find('a', attrs={'class': 'result-title hdrlnk'}).getText().strip()
            except AttributeError:
                job_title = "null"
            home_url = "https://fortcollins.craigslist.org"
            job_link = "%s%s" % (home_url, elem.find('a').get('href'))
            try:
                job_addr = elem.find('span', attrs={'class': 'result-hood'}).getText()
                job_addr = re.sub(r'[\(\)]' , '', job_addr)
            except AttributeError:
                job_addr = "null"
            job_posted = elem.find('time').get('datetime').split(" ")[0]
            job_srch = "General Labor"

            df = df.append({'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)

df.to_csv('/Users/tylehman/Desktop/CL.csv', encoding='utf-8', index=False)
end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')