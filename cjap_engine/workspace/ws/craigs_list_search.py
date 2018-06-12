import pandas as pd
import urllib
import re
from bs4 import BeautifulSoup as Soup
import datetime
import time

class CraigsList():

    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    base_url = ['https://fortcollins.craigslist.org/search/jjj?s=',
                'https://denver.craigslist.org/search/jjj?s=',
                'https://boulder.craigslist.org/search/jjj?s=',
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
                job_link = "%s" % (elem.find('a').get('href'))
                try:
                    job_addr = elem.find('span', attrs={'class': 'result-hood'}).getText()
                    job_addr = re.sub(r'[\(\)]' , '', job_addr).lstrip()
                except AttributeError:
                    job_addr = "null"
                job_posted = elem.find('time').get('datetime').split(" ")[0]
                job_srch = "General Labor"

                # Add job info to our dataframe

                df = df.append({'comp_name': comp_name,
                                'job_title': job_title,
                                'job_link': job_link,
                                'job_addr': job_addr,
                                'job_posted': job_posted,
                                'job_srch': job_srch
                                }, ignore_index=True)
    end = time.time()
#     print "Craigs List = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')


# CraigsListPull = CraigsList()
# print CraigsList.df
# CraigsListPull.df.to_csv('/Users/tylehman/Desktop/Job Analytics/cl.csv', encoding='utf-8')
