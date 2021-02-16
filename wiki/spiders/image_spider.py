import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    # By default API will crawl this url and won’t execute any other requests.
    # Most importantly it will not execute start_requests and spider will not visit urls defined in start_urls spider attribute.
    # There will be only one single request scheduled in API - request for resource identified by url argument.
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']
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