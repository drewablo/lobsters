from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

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


soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find('tablesorter', cellpadding=3)
for item in table.findAll('tr')[0:]:
	col = item.findAll('td')
	name = col[0].string
	print name
