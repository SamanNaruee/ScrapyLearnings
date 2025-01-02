import scrapy
from customs.Flexibles import custom_log

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")
        
        
        for book in books:
            title = response.css("h3 a").attrib['title']
            price = response.css("p.price_color::text").get()
