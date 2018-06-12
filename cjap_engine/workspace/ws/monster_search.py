import pandas as pd
import urllib
from bs4 import BeautifulSoup as Soup
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class Monster():

    pd.set_option('max_colwidth', 500)
    df = pd.DataFrame()
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    
    base_url = ['https://www.monster.com/jobs/search/?q=construction&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=food&where=Denver__2C-CO&sort=dt.rv.di&rad=100&page=',
                'https://www.monster.com/jobs/search/?q=labor&where=Denver__2C-CO&sort=dt.rv.di&rad=100&page=',
                'https://www.monster.com/jobs/search/?q=Mechanic&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=oil&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=driver&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=warehouse&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=disability&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=blind&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=deaf&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=manufact&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=retail&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=trade&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=clean&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=customer&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=nonprofit&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                'https://www.monster.com/jobs/search/?q=government&where=Denver__2C-CO&rad=100&sort=dt.rv.di&page=',
                ]

    driver = webdriver.Firefox(capabilities=caps)
    # for page in range(0,30):
    #     page = page + 1
    for link in base_url:
        url = "%s%d" % (link, 0)
        driver.get(url)
        sleep(5)
        jobs = driver.find_elements_by_class_name("flex-row")
        for n in jobs:
            try:
                job_title = n.find_element_by_class_name("title").text
            except:
                job_title = 'null'
            try:
                comp_name = n.find_element_by_class_name("company").text
            except:
                comp_name = 'null'
            try:
                job_addr = n.find_element_by_class_name("location").text
            except:
                job_addr = 'null'
            try:
                job_link1 = n.find_element_by_class_name("title")
                job_link = job_link1.find_element_by_css_selector('a').get_attribute('href')
            except:
                job_link = 'null'
            try:
                job_posted = n.find_element_by_class_name("meta.flex-col").text
            except:
                job_posted = 'null'

                job_srch = "General Labor"

            df = df.append({'comp_name': comp_name,
                            'job_title': job_title,
                            'job_link': job_link,
                            'job_addr': job_addr,
                            'job_posted': job_posted,
                            'job_srch': job_srch
                            }, ignore_index=True)

    driver.quit()
    end = time.time()
#    print "Monster = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')


#MonsterPull = Monster()
#print Monster.df