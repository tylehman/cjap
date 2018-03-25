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

# indeed.com url
base_url = [
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Arvada%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Aurora%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Brighton%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22E%252E%20Aurora%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Fort%20Collins%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Greeley%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Greenwood%20Village%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Lakewood%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Castle%20Rock%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Littleton%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Louisville%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Loveland%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22N%252E%20Lakewood%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Northglenn%2C%20CO%22}]',
    'https://jobs.lowes.com/search-jobs/Colorado?orgIds=1627&alp=6252001-5417618&alt=3&ascf=[{%22key%22:%22campaign%22,%22value%22:%22Westminster%2C%20CO%22}]']

pd.set_option('max_colwidth', 500)  # remove column limits or info will be lost
df = pd.DataFrame()  # Create a new data frame

for a in base_url:
    target = Soup(urllib.urlopen(a), "lxml")

    # This part of the code returns specific job info desired
    targetElements = target.findAll('li')

    for elem in targetElements:
        comp_name = "Lowes"
        try:
            job_title = elem.find('h2').getText()
        except AttributeError:
            job_title = "null"
        home_url = "https://jobs.lowes.com/search-jobs"
        try:
            job_link = "%s%s" % (home_url, elem.find('a').get('href'))
        except AttributeError:
            job_link = "null"
        try:
            job_addr = elem.find('span', attrs={'class': 'job-location'}).getText()
        except AttributeError:
            job_addr = "null"
        job_posted = "null"
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

base_url = 'http://gh-phipps-construction.careerplug.com/account?embed=1'

target = Soup(urllib.urlopen(base_url), "lxml")
# This part of the code returns specific job info desired
targetElements = target.findAll('div', attrs={'class': 'row'})  # We're interested in each row (= each job)

for elem in targetElements:
    comp_name = "GH Phipps Construction"
    try:
        job_title = elem.find('span', attrs={'class': 'name'}).getText().strip()
    except AttributeError:
        job_title = "null"
    home_url = "http://gh-phipps-construction.careerplug.com"
    job_link = "%s%s" % (home_url, elem.find('a').get('href'))
    try:
        job_addr = elem.find('div', attrs={'class': 'job-location col-md-3'}).getText()
    except AttributeError:
        job_addr = "null"
    job_posted = "null"
    job_srch = "Construction"

    # Add job info to our dataframe

    df = df.append({'comp_name': comp_name,
                    'job_title': job_title,
                    'job_link': job_link,
                    'job_addr': job_addr,
                    'job_posted': job_posted,
                    'job_srch': job_srch
                    }, ignore_index=True)

base_url = [
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695596560&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695595029&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=7987987941&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695596420&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695595049&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695605244&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695599773&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695602315&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=60749494716&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695597858&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=30059830241&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails',
    'https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695601622&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails']

for a in base_url:
    target = Soup(urllib.urlopen(a), "lxml")

    # This part of the code returns specific job info desired
    targetElements = target.findAll('li')  # We're interested in each row (= each job)

    for elem in targetElements:
        comp_name = "Starbucks"
        try:
            job_title = elem.find('a', attrs={'id': 'Div14'}).getText().strip()
        except AttributeError:
            job_title = "null"
        job_link = "https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695596560&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails"
        # try:
        #    job_link = "%s%s" % (home_url,elem.find('a').get('href'))
        # except AttributeError:
        job_addr = "null"
        # print job_link
        # try:
        #    job_addr = elem.find('span', attrs={'itemprop':'addressLocality'}).getText()
        # except AttributeError:
        job_posted = "null"
        job_srch = "Starbucks"

        # Add job info to our dataframe
        df = df.append({'comp_name': comp_name,
                        'job_title': job_title,
                        'job_link': job_link,
                        'job_addr': job_addr,
                        'job_posted': job_posted,
                        'job_srch': job_srch
                        }, ignore_index=True)
df = df[df.job_title != "null"]

base_url = ['https://fortcollins.craigslist.org/search/jjj?s=',
            'https://denver.craigslist.org/search/jjj?s=',
            'https://boulder.craigslist.org/search/jjj?s='
            ]

page = [0, 100, 200, 300]

for b in page:  # For page 1 - 100, the last page is
    for a in base_url:
        url = "%s%d" % (a, b)  # Get the full url
        target = Soup(urllib.urlopen(url), "lxml")
        targetElements = target.findAll('li',
                                        attrs={'class': 'result-row'})  # We're interested in each row (= each job)

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
            except AttributeError:
                job_addr = "null"
            job_posted = elem.find('time').get('datetime')
            job_srch = "General Labor"

            # Add job info to our dataframe

            df = df.append({'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)

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
                comp_name = elem.find('span', attrs={'itemprop': 'name'}).getText().strip()
            except AttributeError:
                comp_name = "null"
            job_title = elem.find('a', attrs={'class': 'turnstileLink'}).attrs['title']
            home_url = "http://www.indeed.com"
            job_link = "%s%s" % (home_url, elem.find('a').get('href'))
            job_addr = elem.find('span', attrs={'itemprop': 'addressLocality'}).getText()
            job_posted = elem.find('span', attrs={'class': 'date'}).getText()
            job_srch = "General Labor"

            df = df.append({'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)


caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True


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

base_url = [
    'http://www.jobs.net/jobs/american-driveline-systems/en-us/search/?keyword=&location=Colorado'
]

for a in base_url:
    target = Soup(urllib.urlopen(a), "lxml")
    # This part of the code returns specific job info desired
    targetElements = target.findAll('tr') # , attrs={'class': ' resultRow'})
    for elem in targetElements:
        comp_name = "AAMCO"
        try:
            job_title = elem.find('td', attrs={'class': 'job-result-job-title'}).getText()
        except AttributeError:
            job_title = "null"
        try:
            job_link = "%s" %  elem.find('a').get('href')
        except AttributeError:
            job_link = "null"
        try:
            ja = elem.text
            job_addr = re.findall('US-*([^ ]*)', ja)
        except AttributeError:
            job_addr = "null"
        try:
            job_posted = elem.find('td', attrs={'itemprop': 'datePosted'}).getText()
        except AttributeError:
            job_posted = "null"
        job_srch = 'Automotive'

        # Add job info to our dataframe
        df = df.append({'comp_name': comp_name,
                        'job_title': job_title,
                        'job_link': job_link,
                        'job_addr': job_addr,
                        'job_posted': job_posted,
                        'job_srch': job_srch
                        }, ignore_index=True)

base_url = ['http://jobs.bedbathandbeyond.com/?location=Denver%2C%20CO%2C%20United%20States&latitude=39.7392358&longitude=-104.990251&radius=25'
            , 'http://jobs.bedbathandbeyond.com/?location=Denver%2C%20CO%2C%20United%20States&latitude=39.7392358&longitude=-104.990251&radius=25&pg=2']
driver = webdriver.Firefox(capabilities=caps)


for url in base_url:
    driver.get(url)
    target = driver.find_elements_by_xpath('//div[@class="job-innerwrap g-cols"]')
    for elem in target:
        comp_name = "Bed Bath Beyond"
        try:
            job_title = elem.find_element_by_tag_name("div").get_attribute("title")
        except AttributeError:
            job_title = "null"
        home_url = "https://jobs.bedbathandbeyond.com"
        try:
            job_link = "%s%s" % (home_url, elem.find_element_by_tag_name("a").get_attribute("href"))
        except AttributeError:
            job_link = "null"
        try:
            addr = elem.text
            job_addr = re.findall('Beyond([^,]*)', addr)

        except AttributeError:
            job_addr = "null"
        job_posted = "null"
        job_srch = 'Retail'

        # Add job info to our dataframe
        df = df.append({'comp_name': comp_name,
                        'job_title': job_title,
                        'job_link': job_link,
                        'job_addr': job_addr,
                        'job_posted': job_posted,
                        'job_srch': job_srch
                        }, ignore_index=True)

df.to_csv('/Users/tylehman/Desktop/wsfinal.csv', encoding='utf-8')

end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
