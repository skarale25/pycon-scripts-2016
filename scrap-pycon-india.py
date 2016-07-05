import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'pyconindia'
    start_urls = ['https://in.pycon.org/cfp/2016/proposals/']

    def parse(self, response):
        for href in response.css('.row h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('.container-fluid h1::text').extract_first(),
            'author': response.css('.container-fluid b::text').extract_first(),
            'link': response.url,
            }
