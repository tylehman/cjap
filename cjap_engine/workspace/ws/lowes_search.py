import pandas as pd
import urllib
import re
from bs4 import BeautifulSoup as Soup
import datetime
import time
from dateutil import parser

class Lowes():
    base_url = ['https://jobs.lowes.com/search-jobs/Arvada?orgIds=1627&alp=6252001-5417618-5426503-5412199&alt=4',
                'https://jobs.lowes.com/search-jobs/Aurora?orgIds=1627&alp=6252001-5417618-5411363-5412347&alt=4',
                'https://jobs.lowes.com/search-jobs/Brighton?orgIds=1627&alp=6252001-5417618-5411363-5414941&alt=4',
                'https://jobs.lowes.com/search-jobs/Castle%20Rock?orgIds=1627&alp=6252001-5417618-5419891-5416329&alt=4',
                'https://jobs.lowes.com/search-jobs/Colorado%20Springs?orgIds=1627&alp=6252001-5417618-5420926-5417598&alt=4',
                'https://jobs.lowes.com/search-jobs/Fort%20Collins?orgIds=1627&alp=6252001-5417618-5578884-5577147&alt=4',
                'https://jobs.lowes.com/search-jobs/Fountain?orgIds=1627&alp=6252001-5417618-5420926-5422191&alt=4',
                'https://jobs.lowes.com/search-jobs/Glenwood%20Springs?orgIds=1627&alp=6252001-5417618-5422751-5423092&alt=4',
                'https://jobs.lowes.com/search-jobs/Grand%20Junction?orgIds=1627&alp=6252001-5417618-5430806-5423573&alt=4',
                'https://jobs.lowes.com/search-jobs/Greeley?orgIds=1627&alp=6252001-5417618-5583239-5577592&alt=4',
                'https://jobs.lowes.com/search-jobs/Greenwood%20Village?orgIds=1627&alp=6252001-5417618-5412056-5423908&alt=4',
                'https://jobs.lowes.com/search-jobs/Lakewood?orgIds=1627&alp=6252001-5417618-5426503-5427946&alt=4',
                'https://jobs.lowes.com/search-jobs/Littleton?orgIds=1627&alp=6252001-5417618-5412056-5429032&alt=4',
                'https://jobs.lowes.com/search-jobs/Longmont?orgIds=1627&alp=6252001-5417618-5574999-5579276&alt=4',
                'https://jobs.lowes.com/search-jobs/Louisville?orgIds=1627&alp=6252001-5417618-5574999-5429522&alt=4',
                'https://jobs.lowes.com/search-jobs/Loveland?orgIds=1627&alp=6252001-5417618-5578884-5579368&alt=4',
                'https://jobs.lowes.com/search-jobs/Northglenn?orgIds=1627&alp=6252001-5417618-5411363-5433124&alt=4',
                'https://jobs.lowes.com/search-jobs/Parker?orgIds=1627&alp=6252001-5417618-5419891-5434006&alt=4',
                'https://jobs.lowes.com/search-jobs/Pueblo?orgIds=1627&alp=6252001-5417618-5435465-5435464&alt=4',
                'https://jobs.lowes.com/search-jobs/Silverthorne?orgIds=1627&alp=6252001-5417618-5440680-5438878&alt=4',
                'https://jobs.lowes.com/search-jobs/Westminster?orgIds=1627&alp=6252001-5417618-5411363-5443910&alt=4',
                ]

    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    for a in base_url:
        target = Soup(urllib.urlopen(a), "lxml")
        job_table = target.find('section', {'id' : 'search-results-list'})
        targetElements = job_table.findAll('li')

        for elem in targetElements:
            comp_name = "Lowes"
            try:
                job_title = elem.find('h2').getText()
            except AttributeError:
                job_title = "null"
            home_url = "https://jobs.lowes.com/"
            try:
                job_link = "%s%s" % (home_url, elem.find('a').get('href'))
            except AttributeError:
                job_link = "null"
            # To get the date the job was posted, I click into the job link and pull the date posted
            # I also use the join to convert the returned tuple to a string
            job_target = Soup(urllib.urlopen(job_link), "lxml")
            job_target_elements = job_target.find('section', {'class':'job-description'})
            try:
                job_details = job_target_elements.findAll('span', {"class" : "job-date job-info"})
                for det in job_details:
                    job_p = det.getText()
                    job_posted1 = ''.join(re.findall(r'[0-9/]', job_p))
                    job_posted = parser.parse(job_posted1).date()
            except:
                job_posted = 'null'
            try:
                job_addr = elem.find('span', attrs={'class': 'job-location'}).getText()
            except AttributeError:
                job_addr = "null"
            job_srch = 'Retail'

            # Add job info to our dataframe
            df = df.append({'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)

    df = df[df.job_addr != "null"]
    end = time.time()
    print "Lowes = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

    # LowesPull = Lowes()
# print LowesPull.df