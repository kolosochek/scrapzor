# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThaipropertyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    sku = scrapy.Field()
    hash = scrapy.Field()
    # type and category
    category = scrapy.Field()
    type = scrapy.Field()
    price_rent = scrapy.Field()
    price_sale = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    description = scrapy.Field()
    features = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    image_url = scrapy.Field()
    images = scrapy.Field()
    # geolocation
    location = scrapy.Field()
    gps = scrapy.Field()
    # ad state
    #isPublished = scrapy.Field()
    isRented = scrapy.Field()
