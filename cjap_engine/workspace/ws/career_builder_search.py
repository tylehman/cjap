import pandas as pd
import urllib
from bs4 import BeautifulSoup as Soup
import re
import datetime
import time

pd.set_option('max_colwidth', 500)
df = pd.DataFrame()

class CareerBuilder():

    base_url = ['https://www.careerbuilder.com/jobs-construction-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-food-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-labor-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-Mechanic-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-oil-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-trucker-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                ]

    for page in range(0,10):
        page = page + 1
        for link in base_url:

            url = "%s%d" % (link, page)
            target = Soup(urllib.urlopen(url), "lxml")
            target_elements = target.findAll('div', attrs={'class':'job-row'})

            for elem in target_elements:
                try:
                    comp_name = elem.find('div', attrs={'class': 'columns large-2 medium-3 small-12'}).getText().strip()
                except AttributeError:
                    comp_name = "null"
                try:
                    job_title = elem.find('h2', attrs={'class': 'job-title hide-for-medium-up'}).getText().strip()
                except AttributeError:
                    job_title = "null"
                home_url = "https://www.careerbuilder.com"
                job_link = "%s%s" % (home_url, elem.find('a').get('href'))
                try:
                    job_addr1 = elem.find('div', attrs={'class': 'columns end large-2 medium-3 small-12'}).getText().strip()
                    job_addr2 = job_addr1.encode('ascii', 'ignore')
                    job_addr = re.findall(r'^[^,]*', job_addr2)
                except AttributeError:
                    job_addr = "null"
                try:
                    job_posted = elem.find('div', {'class':'show-for-medium-up'}).getText().strip()
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
    print "Career Builder = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
    print page

# CareerBuilderPull = CareerBuilder()
# print CareerBuilder.df