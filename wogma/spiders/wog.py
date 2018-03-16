# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wogma.items import WogmaItem




class WogSpider(CrawlSpider):
    name = 'wog'
    #allowed_domains = ['https://wogma.com/']
    start_urls = ['https://wogma.com/movies/basic/']
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('div.button.related_pages.review',)),
             callback="parse_review_page",
             follow=False),)
   

    
    def parse_review_page(self, response):
        
        
        

        reviews = response.css("div.wogma-review").extract()
        rating = response.css("div.col-md-4 p.coloring").extract()
        
        for item in zip(reviews, rating):
            #create a dictionary to store the scraped info
            scraped_info = {
                
                'reviews' : item[0],
                'rating' : item[1],
            }
            yield scraped_info


        
        
        
