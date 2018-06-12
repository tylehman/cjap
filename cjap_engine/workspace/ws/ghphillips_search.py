import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time

class GhPhillips():

    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True

    base_url = 'https://gh-phipps-construction.careerplug.com/account?embed=1'
    driver = webdriver.Firefox(capabilities=caps)
    driver.get(base_url)

    line = driver.find_elements_by_xpath('//div[@id="job_table"]//div[@class="row"]')
    for elem in line:
        comp_name = "GH Phipps Construction"
        try:
            job_title = elem.find_element_by_class_name("name").text
        except AttributeError:
            job_title = "null"
        home_url_2 = "/apps/new"
        job_link = "%s%s" % ( elem.find_element_by_tag_name("a").get_attribute("href"), home_url_2)
        try:
            job_addr = elem.find_element_by_class_name("job-location.col-md-3").text
        except AttributeError:
            job_addr = "null"
        job_posted = "null"
        job_srch = "Construction"

        df = df.append({'comp_name': comp_name,
                        'job_title': job_title,
                        'job_link': job_link,
                        'job_addr': job_addr,
                        'job_posted': job_posted,
                        'job_srch': job_srch
                        }, ignore_index=True)
    driver.quit()
    end = time.time()
    
    # print "GH Phillips = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
#
# ghclass = GhPhillips
# print ghclass.df