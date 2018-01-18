#Top Matter

import scrapy

class Spider(scrapy.Spider):
    name = "nextpagedatabooks" # the name you use in the terminal call "scrapy crawl <name>"
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

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
