import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["qq.com"]
    start_urls = ["https://www.qq.com/"]

    def parse(self, response):
        hrefs=response.xpath('//div[@id ="qqhome-command-area"]//a[@class="linkto"]/@href').extract()
        print(hrefs)
        pass
