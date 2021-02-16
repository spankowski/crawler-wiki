# INSTRUCTION 
- Create docker image From DOCKERFILE
`docker build -t <image_docker_name> .`

### Example: 
`docker build -t crawler_site_api .`

# Running Crawler API: 

- !! Create local_folder inside scrapy project !!

- Run Created image with parameters:

`sudo docker run -p 9080:9080 -tid -v <localization_of_scrapy_project>:/scrapyrt/project <image_docker_name>`

### Example: 
`sudo docker run -p 9080:9080 -tid -v <localization_of_scrapy_project>:/scrapyrt/project crawler_site_api`

# Test Crawler API (Postman)
### Requests 
- get: 
`http://localhost:9080/crawl.json?`
- parameters:
    * url=<site_url>
    * spider_name=<spider_name>

### Example:
`http://localhost:9080/crawl.json?url=https://en.wikipedia.org/wiki/Eiffel_Tower&spider_name=text_spider`

# Spiders to use: 
- text_spider - crawl all text from site

- image_spider - crawl all images from site

# DOWNLOAD RESULTS: 
SSH/FTP - folder: 
- images: local_folder\full
- text: local_folder\text


# Status
- Scrapyrt returns crawler status/or Err if exist