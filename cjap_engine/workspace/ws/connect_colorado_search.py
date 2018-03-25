import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import numpy
import datetime
import time
from dateutil import parser

class ConnectColorado():
    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()

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
        sleep(5)
        # driver.implicitly_wait(20)
        # driver.implicitly_wait(20)
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
            job_link = 'Go to: https://www.connectingcolorado.com   +++++++++   Job Id:',elem[4]
            job_posted1 = elem[3]
            job_posted = parser.parse(job_posted1).date()
            job_srch = "Connect Colorado"

            df = df.append({
                            'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)
    end = time.time()
    print "Connect Colorado = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

# ConnectColoradoPull = ConnectColorado()
# print ConnectColoradoPull.df