import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import time
import datetime
import numpy

start = time.time()
print "start = ", datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

pd.set_option('max_colwidth', 500)  # remove column limits or info will be lost
df = pd.DataFrame()
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
#    print job_list
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

df = df.drop_duplicates(keep='first')

df.to_csv('/Users/tylehman/Desktop/connectCO.csv', encoding='utf-8', index=False)

end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')