import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import numpy
import datetime
import time
from dateutil import parser
import re

class ConnectColorado():
    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    job_values = ['01']
    driver = webdriver.Firefox(capabilities=caps)

    job_values = ['01']
#    job_values = ['01', '02', '05', '11', '12', '18', '19']
    for a in job_values:
        driver.get('https://www.connectingcolorado.com/g_app_quick_js.html')
        sleep(5)

        #This line is broken, full job list is being returned.

        jobs = driver.find_element_by_xpath("//select[@name='emp_category']/option[@value='"+a+"']")
        sleep(8)
        jobs = driver.find_element_by_xpath("//input[@name='Search']")

        window_before = driver.window_handles[0]
        jobs.click()
        sleep(5)
        window_after = driver.window_handles
        sleep(5)
        count = 1
#        target = driver.find_elements_by_class_name('result1')
#         jobs = driver.find_elements_by_tag_name('tr')
        jobs = driver.find_elements_by_xpath('//tr/td[@width="700"]/table[@width="700"]/tbody/tr')

        for job in jobs:
            try:
                job_title = job.find_element_by_class_name('search-results-jobtype').text
            except:
                job_title = 'null'
            print 'job_title = ', job_title
            try:
                job_posted = job.find_element_by_class_name('search-results-date').text
            except:
                job_posted = 'null'
            print 'job_posted = ', job_posted
            try:
                job_posted = job.find_element_by_class_name('search-results-date').text
            except:
                job_posted = 'null'
            print 'job_posted = ', job_posted

        # driver.quit()



#         job_list = []
#         for elem in target:
#             elem = elem.text
#             elem = elem.encode('utf-8')
#             job_list.append(elem)
#             count = count + 1
#         n = count / 7
#         try:
#             job_list = numpy.reshape(job_list, (n,7))
#         except TypeError:
#             pass
#
#         for elem in job_list:
#             comp_name = "Connect Colorado"
#             jt = elem[2]
#             job_title = re.sub(r'^[^a-zA-z]*', '', jt)
# #            print job_title, " : and the type = ", type(job_title)
#             job_addr = elem[5]
#             job_link = 'Go to: https://www.connectingcolorado.com   +++++++++   Job Id:',elem[4]
#             job_posted1 = elem[3]
#             job_posted = parser.parse(job_posted1).date()
#             job_srch = "Connect Colorado"
#
#             df = df.append({
#                             'comp_name': comp_name,
#                             'job_title': job_title,
#                             'job_link': job_link,
#                             'job_addr': job_addr,
#                             'job_posted': job_posted,
#                             'job_srch': job_srch
#                             }, ignore_index=True)

    end = time.time()
#    print "Connect Colorado = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

# ConnectColoradoPull = ConnectColorado()
# print ConnectColoradoPull.df
