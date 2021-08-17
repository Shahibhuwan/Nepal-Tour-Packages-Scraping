# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name =scrapy.Field()
    price =scrapy.Field()
    #description1 =scrapy.Field()
    description2 =scrapy.Field()
    description3 =scrapy.Field()
    description4 =scrapy.Field()
    #discount =scrapy.Field()
    types =scrapy.Field()
    citi =scrapy.Field()
    pass
