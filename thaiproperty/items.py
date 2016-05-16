# -*- coding: utf-8 -*-
from scrapy import Item, Field


class ThaipropertyItem(Item):
    title = Field()
    url = Field()
    sku = Field()
    hash = Field()
    # type and category
    category = Field()
    type = Field()
    price_rent = Field()
    price_sale = Field()
    bedrooms = Field()
    bathrooms = Field()
    area = Field()
    floor = Field()
    description = Field()
    features = Field()
    file_urls = Field()
    files = Field()
    image_url = Field()
    images = Field()
    # geolocation
    location = Field()
    gps = Field()
    # ad state
    isRented = Field()
    #isPublished = Field()
