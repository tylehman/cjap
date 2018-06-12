import pandas as pd
import urllib
from bs4 import BeautifulSoup as Soup
import re
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep




class CareerBuilder():

    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    base_url = ['https://www.careerbuilder.com/jobs-construction-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-food-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-labor-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-Mechanic-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-oil-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-driver-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-warehouse-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-disability-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-blind-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-deaf-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-manufact-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-Retail-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-clean-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-customer-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-non-profit-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
                'https://www.careerbuilder.com/jobs-government-in-denver,co?cat1=&cat2=&cat3=&cb_apply=false&company=&company_id=&emp=all&pay=0&posted=30&radius=50&sort=date_desc&page_number=',
               ]

    driver = webdriver.Firefox(capabilities=caps)
    for page in range(0,10):
        page = page + 1
        for link in base_url:
            url = "%s%d" % (link, page)
            driver.get(url)
            sleep(5)
            jobs = driver.find_elements_by_class_name("job-row")
            for job in jobs:
                try:
                    comp_name = job.find_element_by_class_name('columns.large-2.medium-3.small-12').text
                except:
                    comp_name = "null"
                try:
                    job_title = job.find_element_by_class_name("job-title.show-for-medium-up").text
                except:
                    job_title = "null"
                try:
                    job_link = job.find_element_by_css_selector("a").get_attribute("href")
                except:
                    job_link = "null"
                try:
                    job_addr = job.find_element_by_class_name('columns.end.large-2.medium-3.small-12').text
                except:
                    job_addr = "null"
                try:
                    job_posted = job.find_element_by_class_name('column.small-2.time-posted').text
                except:
                    job_posted = "null"
                try:
                    job_srch = "General Labor"
                except:
                    job_srch = "null"

                df = df.append({'comp_name': comp_name,
                                'job_title': job_title,
                                'job_link': job_link,
                                'job_addr': job_addr,
                                'job_posted': job_posted,
                                'job_srch': job_srch
                                }, ignore_index=True)
    driver.quit()

    end = time.time()
    print "Career Builder = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
    print page


CareerBuilderPull = CareerBuilder()
print CareerBuilder.df
