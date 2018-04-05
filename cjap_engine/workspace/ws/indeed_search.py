import pandas as pd
import urllib
import datetime
import time
from bs4 import BeautifulSoup as Soup

class Indeed():
    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    base_url = ['https://www.indeed.com/jobs?q=general+labor&l=Denver%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=general+labor&l=Fort+Collins%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=Construction&l=Fort+Collins%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=Construction&l=Denver%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=restaurant&l=Denver%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=restaurant&l=Fort+Collins%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=food+service&l=Fort+Collins%2C+CO&radius=100&sort=',
                'https://www.indeed.com/jobs?q=food+service&l=Denver%2C+CO&radius=100&sort='
                ]
    sort_by = 'date'  # sort by date
    start_from = '&start='  # start page number
    count = 0
    for page in range(1, 101):  # For page 1 - 100, the last page is
        page = (page - 1) * 10
        for a in base_url:
            url = "%s%s%s%d" % (a, sort_by, start_from, page)  # Get the full url
            target = Soup(urllib.urlopen(url), "lxml")

            # This part of the code returns specific job info desired
            targetElements = target.findAll('div',
                                            attrs={'class': ' row result'})  # We're interested in each row (= each job)
            for elem in targetElements:
                try:
                    comp_name = elem.find('span', attrs={'class': 'company'}).getText().strip()
                except AttributeError:
                    comp_name = "null"
                try:
                    job_title = elem.find('a', attrs={'rel': 'nofollow'}).attrs['title']
                except AttributeError:
                    job_title = "null"
                home_url = "http://www.indeed.com"
                job_link = "%s%s" % (home_url, elem.find('a').get('href'))
                try:
                    job_addr = elem.find('span', attrs={'class': 'location'}).getText()
                except AttributeError:
                    job_addr = 'null'
                try:
                    job_posted = elem.find('span', attrs={'class': 'date'}).getText()
                except AttributeError:
                    pass
                job_srch = "General Labor"

                df = df.append({'comp_name': comp_name,
                                'job_title': job_title,
                                'job_link': job_link,
                                'job_addr': job_addr,
                                'job_posted': job_posted,
                                'job_srch': job_srch
                                }, ignore_index=True)

    end = time.time()

#     print "Indeed = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')


# IndeedPull = Indeed()
# print Indeed.df
# Indeed.df = Indeed.df.to_csv('/Users/tylehman/Desktop/indeed_COMP_NAME_CHECK.csv', encoding='utf-8', index=False)