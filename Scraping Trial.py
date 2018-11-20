# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:51:07 2018

@author: User2
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests 
url = 'https://www.zomato.com/india'
headers= {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
response = requests.get(url, headers = headers, allow_redirects = False)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
time.sleep(30)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section/div[1]/ul/li[5]/div/a').click()
time.sleep(30)
#driver.find_element_by_xpath('//*[@id="location-suggestion-container"]/div[1]').click()
#time.sleep(10)
driver.find_element_by_xpath('//*[@id="keywords_input"]').click()
driver.find_element_by_xpath('//*[@id="keywords_input"]').send_keys("McDonald's")
driver.find_element_by_xpath('//*[@id="search_button"]').click()
time.sleep(10)

filename = 'database.csv'
f = open(filename, "w")
headers ="Name, Phone 1, Phone 2, Address, Reviewers Name, Reviewers Text, Reviewers Link\n"
f.write(headers)

# Outlet 1
McD_xpath = driver.find_element_by_xpath('/html/body/section/div/div[2]/div[3]/div[2]/div/div[6]/div/div[1]/section/div[1]/div[3]/div[13]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]').click()

# Name of the store
container_1 = driver.find_element_by_xpath('//*[@id="mainframe"]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/h1/a')
name = ''.join(container_1.text).strip()
print("Name: " +name)

# Phone Numbers
ph1_xpath = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[3]/div/div[1]/div[1]/div/div/span/span[1]/span')
ph1 =''.join(ph1_xpath.text).strip()
print('Phone Number 1 :'+ph1)

ph2_xpath = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[3]/div/div[1]/div[1]/div/div/span/span[2]/span')
ph2 =''.join(ph1_xpath.text).strip()
print('Phone Number 2 :'+ph2)

#Address
container_3 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[3]/div/div[2]/div[3]/div[1]/div/span')
address = ''.join(container_3.text).strip()
final_address = address.replace(",", "")
print("Address: " +final_address)

#Reviews link
reviews = driver.find_element_by_link_text('Reviews').click()
time.sleep(30)

# All Reviews Path
all_reviews = driver.find_element_by_xpath('//*[@id="selectors"]/a[2]').click()
time.sleep(30)

# LOAD MORE XPATH
Load_more = driver.find_element_by_xpath('//*[@id="reviews-container"]/div[1]/div[3]/div/div/div[2]/div[1]/span[1]').click()
time.sleep(30)

# Reviewers name
reviewers_name_xpath = '/html/body/div[5]/div[1]/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[8]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/a'
reviewers_name = driver.find_element_by_xpath(reviewers_name_xpath).text.strip()
print("Reviewer's name: " +reviewers_name)

# Reviewers text
reviewers_text_xpath = driver.find_element_by_xpath('//*[@id="reviews-container"]/div[1]/div[3]/div/div/div/div[8]/div/div[1]/div[3]')
reviewers_text = ''.join(reviewers_text_xpath.text)
print("Reviewer's Text: "+reviewers_text)

# Reviewers link
link_xpath = '/html/body/div[5]/div[1]/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[8]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/a'
link = driver.find_element_by_xpath(link_xpath).click()
href = driver.current_url
print("Reviewers link: "+href)

f.write(name+","+ph1+","+final_address+","+reviewers_name+","+reviewers_text+","+href+ "\n")

driver.back()
driver.back()
driver.back()


# Outlet 2
McD_xpath = driver.find_element_by_xpath('//*[@id="orig-search-list"]/div[5]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]').click()

# name of the store
container_1 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/h1/a')
name = ''.join(container_1.text).strip()
print("Name: " +name)

# Phone Numbers
ph1_xpath = driver.find_element_by_xpath('//*[@id="phoneNoString"]/span/span/span')
ph1 =''.join(ph1_xpath.text).strip()
print('Phone Number  :'+ph1)

#Address
container_3 = driver.find_element_by_xpath('//*[@id="mainframe"]/div[1]/div/div[3]/div[3]/div/div[2]/div[3]/div[1]/div/span')
address = ''.join(container_3.text).strip()
final_address = address.replace(",", "")
print("Address: " +final_address)

#Reviews link
reviews = driver.find_element_by_link_text('Reviews').click()
time.sleep(30)

# All Reviews Path
all_reviews = driver.find_element_by_xpath('//*[@id="selectors"]/a[2]').click()
time.sleep(30)

# LOAD MORE XPATH
load_more = driver.find_element_by_xpath('//*[@id="reviews-container"]/div[1]/div[3]/div/div/div[2]/div[1]/span[1]').click()
time.sleep(30)

# Reviewers name
reviewers_name_xpath = '//*[@id="reviews-container"]/div[1]/div[3]/div/div/div/div[7]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/a'
reviewers_name = driver.find_element_by_xpath(reviewers_name_xpath).text.strip()
print("Reviewer's name: " +reviewers_name)

# Reviewers text
reviewers_text_xpath = driver.find_element_by_xpath('//*[@id="reviews-container"]/div[1]/div[3]/div/div/div/div[7]/div/div[1]/div[3]')
reviewers_text = ''.join(reviewers_text_xpath.text)
print("Reviewer's Text: "+reviewers_text)

# Reviewers link
link_xpath = '//*[@id="reviews-container"]/div[1]/div[3]/div/div/div/div[7]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/a'
link = driver.find_element_by_xpath(link_xpath).click()
href = driver.current_url
print("Reviewers link: "+href)

f.write(name+","+ph1+","+final_address+","+reviewers_name+","+reviewers_text+","+href+ "\n")
f.close()
driver.quit()
