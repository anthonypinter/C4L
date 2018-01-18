#Top Matter

import scrapy

class Spider(scrapy.Spider):
    name = "pagedatabooks" # the name you use in the terminal call "scrapy crawl <name>"
    start_urls = [ # the URLs you're scraping
        'http://books.toscrape.com/catalogue/page-1.html',
        'http://books.toscrape.com/catalogue/page-2.html',
    ]

    def parse(self, response):
        for entry in response.css('article.product_pod'):
                    yield {
                        'title': entry.css("article.product_pod a[title]::text").extract_first(),
                        'price': entry.css("p.price_color::text").extract_first(),
                    }
