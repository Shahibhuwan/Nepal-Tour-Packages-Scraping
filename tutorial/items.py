# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title =scrapy.Field()
    price =scrapy.Field()
    duration =scrapy.Field()
    discount =scrapy.Field()
    types =scrapy.Field()
    citi =scrapy.Field()
    pass
