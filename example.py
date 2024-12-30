import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["divar.ir"]
    start_urls = ["https://divar.ir"]

    def parse(self, response):
        pass
