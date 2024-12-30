import scrapy  


class QuotesSpider(scrapy.Spider):  
    name = "quotes"  
    start_urls = [  
        "https://quotes.toscrape.com/tag/humor/",  
    ]  

    custom_settings = {  
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'  
    }  

    def parse(self, response):  
        for quote in response.css("div.quote"):  
            yield {  
                "author": quote.xpath("span/small/text()").get(),  
                "text": quote.css("span.text::text").get(),  
            }  

        next_page = response.css('li.next a::attr("href")').get()  
        if next_page is not None:  
            yield response.follow(next_page, self.parse)