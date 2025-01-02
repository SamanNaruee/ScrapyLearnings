import scrapy
from customs.Flexibles import custom_log

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        title = response.css("h3 a::attr(title)").get()
        price = response.xpath("//p[@class='price_color']").get()
        
        print("####", title, price)

        yield {
            'title': title,
            'price': price
        }
