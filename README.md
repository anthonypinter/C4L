# c4lscrapingworkshop

Link to the slide deck: https://docs.google.com/presentation/d/1zqUPexE_GaRRFGVW4GWyBQy6O6pzqf-smV4M3pyDXlc/edit?usp=sharing

Once you clone this project to your preferred destination, cd into that destination and run:
```
cd c4lscrapingworkshop
cd codetemplates
cd tutorial
```

This will put you into the Scrapy tutorial file.

##Scraping the entire page and saving its HTML

The first task we're going to accomplish is to scrape a single page's HTML source code from http://books.toscrape.com and save it.

Once you are in the tutorial directory in your cmd/terminal, you can run the following command

```
scrapy crawl htmlbooks
```

If you open the tutorial directory in a file explorer/finder, you'll notice that you now have a new html file. You generated this file from (http://books.toscrape.com)! Notice the formatting is not present. Scrapy doesn't get the CSS for page that you scrape, just the HTML code.

Compare your html file to this page: http://books.toscrape.com/catalogue/page-1.html

Notice that all the relevant data is there: title, price, etc.

##Scraping the entire site using next page logic

Next, let's scrape all 50 pages on the website and save their source code (note, this will result in 50 files in your tutorial directory):

```
scrapy crawl nextpagehtmlbooks
```

This is the basic architecture for scraping an entire site's html, and saving it. Why might this be useful?

##Scraping specific pieces of data from the entire website

Now that we have a grasp on how to scrape and save the entire source code, let's turn our attention to scraping specific pieces of data.

```
scrapy crawl pagedatabooks -o out.json
```

This will generate a json output file containing all of the titles of the books on page 1.
