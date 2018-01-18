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

book_selector = 'article.product_pod'
title_selector = 'article.product_pod a[title]'
titles = []
price_selector = 'p.price_color'
prices = []
data = []

def form_url(num):
    input_url = 'http://books.toscrape.com/catalogue/page-%s.html' % num
    return input_url

x = 1

while x <= 2: # we know the site has 50 pages
    url = form_url(x) # calls the function defined above
    print(url) # just a check to make sure everything is working
    driver.get(url) # opens the url
    sleep(delay) # a pause so we are kind to the servers

    found_books = driver.find_elements_by_css_selector(book_selector)

    for book in found_books:
        title = book.find_element_by_css_selector(title_selector).text
        print title
        titles.append(title)
        price = book.find_element_by_css_selector(price_selector).text
        print price
        prices.append(price)



        out_data = dict([('price', price), ('title', title)])
        print out_data
        data.append(out_data)
        print data

    x += 1 # adds one to our counter

length = len(titles)
print length

#proper JSON output here

with open('data.json', 'wb') as f:
    json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)

driver.quit()
