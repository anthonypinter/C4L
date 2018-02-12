from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import codecs
import json
import datetime

# only edit these if you're having problems
delay = 1  # time to wait on each page load before reading the page
driver = webdriver.Safari()  # options are Chrome() Firefox() Safari()

def form_url(num):
    input_url = 'http://books.toscrape.com/catalogue/page-%s.html' % num
    return input_url

x = 1

while x <= 2: # we know the site has 50 pages
    url = form_url(x) # calls the function defined above
    print(url) # just a check to make sure everything is working
    driver.get(url) # opens the url
    sleep(delay) # a pause so we are kind to the servers

    page = driver.page_source
    completeName = 'page-%s.html' % x
    print completeName
    outfile = codecs.open(completeName, "w", "utf-8")
    print outfile

    outfile.write(page)

    x += 1 # adds one to our counter

driver.quit()
