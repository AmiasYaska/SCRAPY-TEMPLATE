import scrapy


class NewsSpider(scrapy.Spider):
    name = "amias"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
