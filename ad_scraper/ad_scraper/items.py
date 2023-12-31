# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdScraperItem(scrapy.Item):
    
    # define the fields for your item here like:
    productName = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    imageURL = scrapy.Field()
    operatingSystem = scrapy.Field()
    displayTechnology = scrapy.Field()
    
