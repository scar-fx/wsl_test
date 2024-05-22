import scrapy
from wsl.wsl.items import WslItem
from time import sleep


class JssSpider(scrapy.Spider):
    name = "jss"
    allowed_domains = ["quotes.toscrape.com"]

    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(url, meta={'playwright': True})


    def parse(self, response):
        sleep(3)

        for quote in response.css('div.quote'):
            sleep(1)
            quote_item = WslItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
        pass
