from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep
import re

while True:
	fp =webdriver.FirefoxProfile('C:\Users\drew\AppData\Roaming\Mozilla\Firefox\Profiles\snwydtpt.default')
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
	ev = driver.find_elements_by_class_name("even")
	od = driver.find_elements_by_class_name("odd")
	leng = len(ev) + len(od)
	if z < leng:
		for people in soup.findAll('a',href=True):
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
						for item in table:
							y = str(y)
							element = driver.find_element_by_xpath('//table[2]/tbody/tr[4]/td/div/table/tbody/tr['+y+']/td[2]/font/a')
							y = int(y) 
							element.click()
							y+=1
							print y
							html_source = driver.page_source
							soup = BeautifulSoup(html_source)
							if soup.find('table', id='tabTwo'):
								element = driver.find_element_by_xpath("//tr[2]/td[6]/font/a")	
								element.click()			
								driver.back()
								sleep(10)										
			z+=1
			driver.back()
			
