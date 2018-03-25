# load the library
import pandas as pd
import urllib
import re
from time import sleep
import numpy
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
        home_url = "https://jobs.lowes.com/"
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
    targetElements = target.findAll('li')  # We're interested in each row (= each job)

    for elem in targetElements:
        comp_name = "Starbucks"
        try:
            job_title = elem.find('a', attrs={'id': 'Div14'}).getText().strip()
        except AttributeError:
            job_title = "null"
        job_link = "https://wfa.kronostm.com/index.jsp?INDEX=0&LOCATION_ID=695596560&locale=en_US&applicationName=StarbucksNonReqExt&SEQ=locationDetails"
        job_addr = "null"
        job_posted = "null"
        job_srch = "Starbucks"

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
            try:
                job_title = elem.find('a', attrs={'rel': 'nofollow'}).attrs['title']
            except AttributeError:
                job_title = "null"
            home_url = "http://www.indeed.com"
            job_link = "%s%s" % (home_url, elem.find('a').get('href'))
            try:
                job_addr = elem.find('span', attrs={'itemprop': 'addressLocality'}).getText()
            except AttributeError:
                pass
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

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

base_url = ['https://www.connectingcolorado.com/e_app_quick_js.html']

job_values = ['37', '47', '45', '35', '49']
for a in job_values:
    driver = webdriver.Firefox(capabilities=caps)
    driver.get("https://www.connectingcolorado.com/e_app_quick_js.html")
    jobs = driver.find_element_by_id("city")
    jobs.send_keys("Denver Metro")
    sleep(5)
    jobs = driver.find_element_by_xpath("//select[@name='job_category']/option[@value='"+a+"']")
    sleep(8)
    jobs = driver.find_element_by_xpath('//img[@src="/images/button-go-up.gif"]')
    window_before = driver.window_handles[0]
    jobs.click()
    driver.implicitly_wait(10)
    driver.implicitly_wait(10)
    window_after = driver.window_handles
    sleep(5)
    count = 1
    target = driver.find_elements_by_class_name('result1')

    job_list = []
    for elem in target:
        elem = elem.text
        elem = elem.encode('utf-8')
        job_list.append(elem)
        count = count + 1
    n = count / 7
    try:
        job_list = numpy.reshape(job_list, (n,7))
    except TypeError:
        pass

    for elem in job_list:
        comp_name = "Connect Colorado"
        job_title = elem[2]
        job_addr = elem[5]
        job_link = elem[4]
        job_posted = elem[3]
        job_srch = "Connect Colorado"

        df = df.append({
                        'comp_name': comp_name,
                        'job_title': job_title,
                        'job_link': job_link,
                        'job_addr': job_addr,
                        'job_posted': job_posted,
                        'job_srch': job_srch
                        }, ignore_index=True)

#df = df.drop_duplicates(keep='first')

df = df.to_csv('/Users/tylehman/Desktop/python/sqlite/wsfinal.csv', encoding='utf-8', index=False)
df = pd.read_csv('/Users/tylehman/Desktop/python/sqlite/wsfinal.csv')

df = df.replace({r' - ': '', r'(\[)': '', r']': ''}, regex=True)
df.to_csv('/Users/tylehman/Desktop/python/sqlite/wsfinal.csv', encoding='utf-8', index=False)

df = pd.read_csv('/Users/tylehman/Desktop/python/sqlite/wsfinal.csv')

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
two_day = datetime.timedelta(days=2)
three_day = datetime.timedelta(days=3)
four_day = datetime.timedelta(days=4)
five_day = datetime.timedelta(days=5)
six_day = datetime.timedelta(days=6)
seven_day = datetime.timedelta(days=7)
eight_day = datetime.timedelta(days=8)
nine_day = datetime.timedelta(days=9)
ten_day = datetime.timedelta(days=10)
eleven_day = datetime.timedelta(days=11)
twelve_day = datetime.timedelta(days=12)
thirteen_day = datetime.timedelta(days=13)
fourteen_day = datetime.timedelta(days=14)
fifteen_day = datetime.timedelta(days=15)
sixteen_day = datetime.timedelta(days=16)
seventeen_day = datetime.timedelta(days=17)
eighteen_day = datetime.timedelta(days=18)
nineteen_day = datetime.timedelta(days=19)
twenty_day = datetime.timedelta(days=20)
twentyone_day = datetime.timedelta(days=21)
twentytwo_day = datetime.timedelta(days=22)
twentythree_day = datetime.timedelta(days=23)
twentyfour_day = datetime.timedelta(days=24)
twentyfive_day = datetime.timedelta(days=25)
twentysix_day = datetime.timedelta(days=26)
twentyseven_day = datetime.timedelta(days=27)
twentyeight_day = datetime.timedelta(days=28)
twentynine_day = datetime.timedelta(days=29)
thirty_day = datetime.timedelta(days=30)

day1 = today - one_day
day2 = today - two_day
day3 = today - three_day
day4 = today - four_day
day5 = today - five_day
day6 = today - six_day
day7 = today - seven_day
day8 = today - eight_day
day9 = today - nine_day
day10 = today - ten_day
day11 = today - eleven_day
day12 = today - twelve_day
day13 = today - thirteen_day
day14 = today - fourteen_day
day15 = today - fifteen_day
day16 = today - sixteen_day
day17 = today - seventeen_day
day18 = today - eighteen_day
day19 = today - nineteen_day
day20 = today - twenty_day
day21 = today - twentyone_day
day22 = today - twentytwo_day
day23 = today - twentythree_day
day24 = today - twentyfour_day
day25 = today - twentyfive_day
day26 = today - twentysix_day
day27 = today - twentyseven_day
day28 = today - twentyeight_day
day29 = today - twentynine_day
day30 = today - thirty_day

df = df.replace({'null' : day30,
                 'Today' : today,
                 'today' : today,
                 'Just posted' : today,
                 '1 day ago': day1,
                 '2 days ago': day2,
                 '3 days ago': day3,
                 '4 days ago': day4,
                 '5 days ago': day5,
                 '6 days ago': day6,
                 '7 days ago': day7,
                 '8 days ago': day8,
                 '9 days ago': day9,
                 '10 days ago': day10,
                 '11 days ago': day11,
                 '12 days ago': day12,
                 '13 days ago': day13,
                 '14 days ago': day14,
                 '15 days ago': day15,
                 '16 days ago': day16,
                 '17 days ago': day17,
                 '18 days ago': day18,
                 '19 days ago': day19,
                 '20 days ago': day20,
                 '21 days ago': day21,
                 '22 days ago': day22,
                 '23 days ago': day23,
                 '24 days ago': day24,
                 '25 days ago': day25,
                 '26 days ago': day26,
                 '27 days ago': day27,
                 '28 days ago': day28,
                 '29 days ago': day29,
                 '30 days ago': day30,
                 '30+ days ago': day30,
                 '+30 days ago': day30,
                 r'\d' : day1,
                 })

df.to_csv('/Users/tylehman/Desktop/python/sqlite/wsfinal.csv', encoding='utf-8')

end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
