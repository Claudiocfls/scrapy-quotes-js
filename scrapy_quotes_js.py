import scrapy
from scrapy.selector import Selector
import urllib

class QuotesSpider(scrapy.Spider):
    name = 'scrapy_quotes_js'
    start_urls = [
        'http://quotes.toscrape.com/js'
    ]
    splash_base_url = 'http://localhost:8050/render.html'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(''.join([self.splash_base_url, '?', urllib.parse.urlencode({ 'url': url })]), callback=self.parse)

    def parse(self, response):
        quotes_blocks = response.xpath('//div[@class="quote"]').extract()
        for quote_block in quotes_blocks:
            quote_text = Selector(text=quote_block).xpath('//span[@class="text"]/text()').get()
            author = Selector(text=quote_block).xpath('//small[@class="author"]/text()').get()
            tags = Selector(text=quote_block).xpath('//div[@class="tags"]/a[@class="tag"]/text()').extract()
            yield {
              'quote': quote_text,
              'author': author,
              'tags': tags
            }
            
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            target_url = urllib.parse.urljoin(self.start_urls[0], next_page)
            next_url = ''.join([self.splash_base_url, '?', urllib.parse.urlencode({ 'url': target_url })])
            yield scrapy.Request(next_url, callback=self.parse)
