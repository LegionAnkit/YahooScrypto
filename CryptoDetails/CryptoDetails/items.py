# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptodetailsItem(scrapy.Item):
    # define the fields for your item here like:
    symbol = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    per_change = scrapy.Field()
    market_cap = scrapy.Field()
    
