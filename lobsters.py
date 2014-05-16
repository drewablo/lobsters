from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import re
import os 


driver = webdriver.Firefox()
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
						element = driver.find_element_by_xpath("//td/font/a")
						element.click()
						windows = driver.window_handles
						expwin = windows[1]
						mainwin = windows[0]
						print windows
						driver.switch_to_window(expwin)
						element = driver.find_element_by_xpath("//div/div[2]/button[4]")
						element.send_keys(Keys.RETURN)
						
			driver.back();		
		'''
		if table.findAll('tr')[5:]:
			if soup.findAll('a',href=True):
				print soup.findAll('a',href=True)
				element = driver.find_element_by_xpath("//tr/tdfont/a")
				element.click()
				'''
