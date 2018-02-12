# c4lscrapingworkshop

Link to the slide deck: https://docs.google.com/presentation/d/1Rp7mq3_XLlucbBlu0WWH8ooTffhV2MMK53YYEd6l2-k/edit?usp=sharing

## Scrapy

Once you clone this project to your preferred destination, cd into that destination and run:
```
cd c4lscrapingworkshop
cd codetemplates
cd scrapy
```

This will put you into the Scrapy tutorial file.

### Scraping the entire page and saving its HTML

The first task we're going to accomplish is to scrape a single page's HTML source code from http://books.toscrape.com and save it.

Once you are in the tutorial directory in your cmd/terminal, you can run the following command

```
scrapy crawl htmlbooks
```

If you open the tutorial directory in a file explorer/finder, you'll notice that you now have a new html file. You generated this file from (http://books.toscrape.com)! Notice the formatting is not present. Scrapy doesn't get the CSS for page that you scrape, just the HTML code.

Compare your html file to this page: http://books.toscrape.com/catalogue/page-1.html

Notice that all the relevant data is there: title, price, etc.

### Scraping the entire site using next page logic

Next, let's scrape all 50 pages on the website and save their source code (note, this will result in 50 files in your tutorial directory):

```
scrapy crawl nextpagehtmlbooks
```

This is the basic architecture for scraping an entire site's html, and saving it. Why might this be useful?

### Scraping specific pieces of data from the entire website

Now that we have a grasp on how to scrape and save the entire source code, let's turn our attention to scraping specific pieces of data.

```
scrapy crawl pagedatabooks -o out.json
```

This will generate a json output file containing all of the titles of the books on page 1. Let's do an exercise - update this file so that you also pull the price of each book. To help you with this, you can use the developer's terminal to view the source code and see what the CSS selector is for the price, or you can use [Selector Gadget](http://selectorgadget.com).

If you're having trouble, the answer can be found in the `answer_pagedatabooks.py` file in the `scrapy/tutorial/spiders` directory.

### Scraping specific pieces of data from the entire website

Time for the next exercise! At this point, you've seen how to select certain elements to scrape, and you've seen how to scrape multiple pages using the next page logic built into Scrapy.

Now, combine the two!

Create a script that scrapes the titles, prices, and any other data you want off of every page on http://books.toscrape.com. (Hint: copy+paste from other files is always a good way to go!)

If you'd like to check your script against mine, open the `nextpagedatabooks.py` file found in `scrapy/tutorial/spiders`.

## Selenium

Selenium can be used to accomplish similar tasks, albeit in a different manner.

To use the selenium skeletons, navigate to the selenium directory in the repository.

```
cd c4l
cd codetemplates
cd selenium
```

Then run them using

`python <filename>.py`

## Free Time

The original Scrapy tutorial uses http://quotes.toscrape.com. This is useful for us, because you can test your skills on that site, and have the answers available [here](https://docs.scrapy.org/en/latest/intro/tutorial.html).

Alternatively, you can try to scrape a different site. The basic code will remain the same, what will change is the URLs and CSS selectors.
