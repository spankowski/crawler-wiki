import scrapy


class TextSpider(scrapy.Spider):
    name = 'text'
    # start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        text = response.xpath('//text()').getall()
        str_save = ''.join(text)
        with open('local_folder/text/result.txt', 'w', encoding='utf-8') as html_file:
                html_file.write(str_save)
