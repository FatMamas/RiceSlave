__author__ = 'Gyfis'

import scrapy

from items import WebstaItem


class WebstaMeSpider(scrapy.Spider):
    name = 'websta_me'
    allowed_domains = ['websta.me']
    # can be parametrized

    # 'http://websta.me/tag/sushirolls?npk=971095417679230582'  # sushirolls checkpoint
    # 'http://websta.me/tag/catstagram?npk=1130680514212353312' # castagram checkpoint
    # 'http://websta.me/tag/burger?npk=1130136132082892683'     # burger checkpoint
    start_urls = [
        'http://websta.me/tag/nikeporn?npk=1130953219125326371'
    ]

    max_pages = 0

    def parse(self, response):
        for sel in response.xpath('//div[@class="mainimg_wrapper"]/a/img/@src'):
            item = WebstaItem()
            item['image_urls'] = [sel.extract()]
            yield item

        for sel in response.xpath('//ul[@class="pager"]/li/a/@href'):
            url = response.urljoin(sel.extract())
            yield scrapy.Request(url, callback=self.parse)
