#Top Matter

import scrapy

class Spider(scrapy.Spider):
    name = "nextpagehtmlbooks" # the name you use in the terminal call "scrapy crawl <name>" or "scrapy crawl <name> -o <name>.json"
    start_urls = [ # the URLs you're scraping
        'http://books.toscrape.com/catalogue/page-1.html',
    ]

    def parse(self, response):
        page = response.url.split("/")[-1] # splits the URL provided and takes everything after the second '/' to be used as a page name
        filename = 'books-%s' % page # sets the file name that we'll save to using the split we set in line 12
        with open(filename, 'wb') as f: # opens a file with the name we set in line 13
            f.write(response.body) # writes the HTML for the webpage we opened

        next_page = response.css('li.next a::attr(href)').extract_first() #looks for the next page element on the page        if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
