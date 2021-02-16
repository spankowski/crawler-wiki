import scrapy
import io

class TextSpider(scrapy.Spider):
    name = 'text_spider'
    # By default API will crawl this url and won’t execute any other requests.
    # Most importantly it will not execute start_requests and spider will not visit urls defined in start_urls spider attribute.
    # There will be only one single request scheduled in API - request for resource identified by url argument.
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        text = response.xpath('//text()').getall()
        str_save = ''.join(text)
        with io.open('local_folder/text/result.txt', 'w', encoding='utf-8') as html_file:
                html_file.write(str_save)
        # text save
        yield {
            'text' : str_save
        }