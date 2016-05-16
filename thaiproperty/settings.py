# -*- coding: utf-8 -*-
BOT_NAME = 'thaiproperty'
#
SPIDER_MODULES = ['thaiproperty.spiders']
NEWSPIDER_MODULE = 'thaiproperty.spiders'
DEFAULT_ITEM_CLASS = 'thaiproperty.items.ThaipropertyItem'
# save images
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
FILES_STORE = '/data/sc/images/'
# speed settings
CONCURRENT_REQUESTS=32
DOWNLOAD_DELAY=1
