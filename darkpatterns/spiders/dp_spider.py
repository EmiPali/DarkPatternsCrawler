import scrapy
from ..items import DarkpatternsItem
from selenium import webdriver
# chrome_path = r"C:\Users\0190678225\Anaconda3\bin\chromedriver_win32"
# driver = webdriver.Chrome(chrome_path)

class Dpspider(scrapy.Spider):
    # driver = webdriver.Chrome('C:\webdrivers')
    # driver.get("https://twitter.com/hashtag/darkpatterns?lang=en")

    name = 'dp'
    start_urls= [
        'https://twitter.com/hashtag/darkpatterns?lang=en'
            ]

    def parse(self, response):
        items = DarkpatternsItem()
        all_descriptions = response.css('div.css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll')
     

        for descriptions in all_descriptions:
            author = descriptions.css('span.css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0::text').extract()
            hour = descriptions.css('time::text').extract()
            status = descriptions.css('div.css-1dbjc4n::text').extract()
            items['author'] = author
            items['hour'] = hour
            items['status'] = status
            yield items
