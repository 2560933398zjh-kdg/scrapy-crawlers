import scrapy


class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=mobile+phones&crid=25B6PNITR9XSH&sprefix=mobile%2Caps%2C1190&ref=nb_sb_ss_p13n-expert-pd-ops-ranker_1_6"]

    def parse(self, response):
        print(response.xpath('//div[@class="sg-col-inner"]//h2/text()').extract())
