from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request
#from send_email import test_sendmail
import time
from text_unidecode import unidecode

class CraigsScraper(object):
	def __init__(self, location, postal, max_price, radius):
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius

		self.url = f"https://{location}.craigslist.org/search/search_distance={radius}&postal={postal}&max_price={max_price}"

		self.driver = webdriver.Firefox()
		self.delay = 5


	def test(self):
		print(self.url)

location = "annarbor"
postal = "48109"
max_price = 900
radius = 20

scraper = CraigsScraper(location, postal, max_price, radius)
scraper.test()