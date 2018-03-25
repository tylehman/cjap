import pandas as pd
import urllib
from bs4 import BeautifulSoup as Soup
import datetime
import time

pd.set_option('max_colwidth', 500)
df = pd.DataFrame()

class Monster():

    base_url = ['https://www.monster.com/jobs/search/?q=construction&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=food&where=Denver__2C-CO&sort=dt.rv.di&rad=100&page=',
                'https://www.monster.com/jobs/search/?q=labor&where=Denver__2C-CO&sort=dt.rv.di&rad=100&page=',
                'https://www.monster.com/jobs/search/?q=Mechanic&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=oil&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=trucker&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                ]

    for page in range(0,30):
        page = page + 1
        for link in base_url:

            url = "%s%d" % (link, page)
            target = Soup(urllib.urlopen(url), "lxml")
            target_elements = target.findAll('div', attrs={'class':'js_result_details'})

            for elem in target_elements:
                try:
                    comp_name = elem.find('div', attrs={'class': 'company'}).getText().strip()
                except AttributeError:
                    comp_name = "null"
                try:
                    job_title = elem.find('div', attrs={'class': 'jobTitle'}).getText().strip()
                except AttributeError:
                    job_title = "null"
                job_link = "%s" % ( elem.find('a').get('href'))
                try:
                    job_addr = elem.find('div', attrs={'class': 'job-specs job-specs-location'}).getText().strip()
                except AttributeError:
                    job_addr = "null"
                try:
                    job_posted = elem.find('time').getText()
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
    print "Monster = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

# MonsterPull = Monster()
# print Monster.df