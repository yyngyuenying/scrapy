import scrapy

class firstSpider(scrapy.Spider):
   name = 'firstscrapy'
#   allowed_domains ['hk01.com']
   start_urls = ('https://www.hk01.com/',)

   def parse(self, response):
     filename = response.url.split('/')[-2]
     with open(filename, 'wb') as f:
       f.write(response.body)     
