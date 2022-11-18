import scrapy

class myproduct(scrapy.Spider):
    name='productname'
    start_urls=['http://books.toscrape.com/']

    def parse(self, response):

        books=response.css('div.col-sm-8.col-md-9').extract()

        header=books.css("h1::text").extraxt()

        yield {'header':header}