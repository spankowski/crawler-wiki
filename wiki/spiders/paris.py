import scrapy


class ParisSpider(scrapy.Spider):
    name = 'paris'
    # start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']
    # parsowanie 
    def parse(self, response):
        raw_image_urls = response.css('img').xpath('@src').getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        # clean image urls as list
        yield {
            'image_urls' : clean_image_urls
        }