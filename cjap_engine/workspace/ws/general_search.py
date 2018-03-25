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

class Base:

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver