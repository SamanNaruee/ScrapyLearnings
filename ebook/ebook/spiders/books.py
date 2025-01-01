import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        custom_log(response.css("h3 a").get())


def custom_log(value):
    print("##############################")
    print(f"Your value:\n{value}")
