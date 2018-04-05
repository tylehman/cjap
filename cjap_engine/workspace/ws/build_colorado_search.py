import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time

class BuildColorado():
    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

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
        end = time.time()
        # print "Build Colorado = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')


# BuildColoradoPull = BuildColorado()
# print BuildColoradoPull.df