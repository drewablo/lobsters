from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep
import re

fp =webdriver.FirefoxProfile('/home/andrewpt85/.mozilla/firefox/todr4fv6.default')
driver = webdriver.Firefox(fp)
driver.get("http://www.ilsos.gov/lobbyistsearch/")
element = driver.find_element_by_xpath("//input[@value='official']")
element.click()
element = driver.find_element_by_xpath("//input[@value='Submit']")
element.click()
select = Select(driver.find_element_by_name('year'))
select.select_by_visible_text("2014")
element = driver.find_element_by_xpath("//input[@value='Submit']")
element.click()
html_source = driver.page_source
soup = BeautifulSoup(html_source)
table = soup.find('table', cellpadding='3')
x=0
y=1
z=1
if table.findAll('tr')[x:]:
	x+=1
	if soup.findAll('a',href=True):
		element = driver.find_element_by_class_name("db10ub")
		element.click()
		elements = driver.find_elements_by_class_name("db10ub")
		html_source = driver.page_source
		soup = BeautifulSoup(html_source)
		table = soup.find('table', cellpadding='3')
		while y < len(elements):
			if soup.findAll('a',href=True):
				y = str(y)
				if driver.find_element_by_xpath("//td[2]/font/a"):
					element = driver.find_element_by_xpath("//tr["+y+"]/td[2]/font/a")
					y = int(y)
					element.click()
					y+=1
					print y
					html_source = driver.page_source
					soup = BeautifulSoup(html_source)
					if soup.find('table', id='tabTwo'):
						element = driver.find_element_by_xpath("//tr[2]/td[6]/font/a")	
						element.click()
						sleep(.1)					
			driver.back()
driver.back()
