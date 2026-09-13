import scrapy
import json

class ElectricalSpider(scrapy.Spider):
    name = "electrical"
    allowed_domains = ["3.cn"]
    start_urls = ["https://dc.3.cn/category/get"]

    def parse(self, response):
        jd_json=json.loads(str(response.body,encoding='gbk'),
                           encoding='gbk')

        result=[]
        for data in jd_json['data']:
            for data2 in data['s']:
                url=data2['n'].split('|')[0]
                title = data2['n'].split('|')[1]

                result.append({
                    "url":url,
                    "title":title
                })
                for data3 in data2['s']:
                    url2 = data2['n'].split('|')[0]
                    title2 = data3['n'].split('|')[1]
                    for data4 in data2['s']:
                        url3 = data2['n'].split('|')[0]
                        title3 = data3['n'].split('|')[1]
        print(result)
        pass