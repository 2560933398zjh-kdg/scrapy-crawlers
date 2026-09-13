import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["qq.com"]
    start_urls = ["https://qq.com"]

    def parse(self, response):
        pass
