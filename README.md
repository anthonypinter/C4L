# c4lscrapingworkshop

Link to the slide deck: https://docs.google.com/presentation/d/1zqUPexE_GaRRFGVW4GWyBQy6O6pzqf-smV4M3pyDXlc/edit?usp=sharing

Once you clone this project to your preferred destination, cd into that destination and run:
'''
cd c4lscrapingworkshop
cd codetemplates
cd tutorial
'''

This will put you into the Scrapy tutorial file. Once you are in the tutorial directory in your cmd/terminal, you can run the following command

'''
scrapy crawl htmlbooks
'''

If you open the tutorial directory in a file explorer/finder, you'll notice that you now have a new html file. You generated this file! Notice that the relevant data is there, but the formatting is not. Scrapy doesn't get the CSS for thing that you scrape.

Compare your html file to this page: http://books.toscrape.com/catalogue/page-1.html

Notice that all the relevant data is there: title, price, etc.
