from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
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
		
		self.driver = webdriver.Firefox(executable_path='/Users/drewscheffer/Downloads/geckodriver')
		self.delay = 3

	def load_craigslist_url(self):
		self.driver.get(self.url)
		try:

			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform")))
			print("page is ready")
		except TimeoutException:
			print("Loading took too much time")

	def extract_post_titles(self):
		all_posts = self.driver.find_elements_by_class_name("result-row")
		post_title_list = []
		for post in all_posts:
			print(post.text)
			post_title_list.append(post.text)
		return post_title_list

	def extract_post_urls(self):
		results = self.driver.find_elements_by_css_selector('.result-row')
		a = results[0].find_element_by_css_selector('.result-info')
		text = unidecode(a.find_element_by_tag_name('a').text)
		print(text)
	
	
	

location = "annarbor"
postal = "48109"
max_price = 900
radius = 20

scraper = CraigsScraper(location, postal, max_price, radius)
scraper.load_craigslist_url()
#scraper.extract_post_titles()
scraper.extract_post_urls()
