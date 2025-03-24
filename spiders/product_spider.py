import scrapy
import re
import json

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    
    def __init__(self, domains=None, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = domains.split(",") if domains else []
        self.product_patterns = [r'/product/', r'/item/', r'/p/']
        self.visited_urls = set()

    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            absolute_url = response.urljoin(link)

            if absolute_url in self.visited_urls:
                continue
            self.visited_urls.add(absolute_url)

            if any(re.search(pattern, absolute_url) for pattern in self.product_patterns):
                yield {"domain": response.url.split('/')[2], "product_url": absolute_url}
            else:
                yield scrapy.Request(url=absolute_url, callback=self.parse)
