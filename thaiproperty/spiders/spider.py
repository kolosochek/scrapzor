#made by megusta
import scrapy
import re
from thaiproperty.items import ThaipropertyItem
from hashlib import md5
from scrapy.exceptions import DropItem

class ThaipropertySpider(scrapy.Spider):
    #http://www.thaiproperty.com/for_rent/condos.html
    name = 'thaipropertycom_spider'
    start_urls = ['http://www.thaiproperty.com/']
    base_url = "http://www.thaiproperty.com/for_rent/condos.html?&per_page="
    data = []
    page_counter = 0

    # init
    def parse(self, response):
        while(self.page_counter <= 1380 ): #1380):
            url = "%s%s" % (self.base_url, self.page_counter)
            # switching pages
            self.page_counter += 20
            yield scrapy.Request(url, self.parse_pages)

    # get links from category page and make request on each one of it
    def parse_pages(self, response):
        for href in response.css('.subBoxDetailList > a::attr("href")'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, self.parse_ad)

    # scrap the detail ad page
    def parse_ad(self, response):
        file_urls = []
        features = []
        items = {}
        # create Item object
        item = ThaipropertyItem()

        # url
        item['url'] = response.url
        item['hash'] = md5(response.url).hexdigest()
        item['isActive'] = True

        # title
        for title in response.css("#content > h2::text").extract():
            item['title'] = title.strip()

        # sku
        for sku in response.css(".boxRightContent > div > h4::text").extract():
            result = ''
            if u"::" in sku:
                result = sku.split('::')
                try:
                    result = result[::-1][0]
                except IndexError:
                    print("Can't split sku!")
            item['sku'] = result.strip()


        # floor
        for floor in response.css(".boxRightContent > div> ul > li:contains('Floor : ')::text").extract():
            item['floor'] = floor.replace('Floor : ', '')

        # rent price by month
        for month_rent_price in response.css("span#boxpriceShow2::text").extract():
            item['price_rent'] = month_rent_price.replace(u'\u0e3f', '').replace(' /m', '') # replace baht currency sign

        # sale price by month
        for sale_price in response.css("#boxpriceShow::text").extract():
            item['price_sale'] = sale_price.replace(u'\u0e3f', '') # replace baht currency sign

        # area
        for area in response.css(".boxRightContent > div> ul > li:contains('Living area : ')::text").extract():
            square = area.replace('Living area : ', '')
            if "sqm." in square:
                square = square.replace('sqm.', '')
            item['area'] = square

        # bedrooms
        for bedrooms in response.css(".boxRightContent > div> ul > li:contains('Bedrooms : ')::text").extract():
            bedrooms_count = bedrooms.replace('Bedrooms : ', '')
            if u'studio' in bedrooms_count.lower():
                bedrooms_count = '1'

            item['bedrooms'] = bedrooms_count

        # bathrooms
        for bathrooms in response.css(".boxRightContent > div> ul > li:contains('Bathrooms : ')::text").extract():
            item['bathrooms'] = bathrooms.replace('Bathrooms : ', '')

        # location
        for location in response.css(".boxRightContent > div> ul > li:contains('Location : ')::text").extract():
            item['location'] = location.replace('Location : ', '')

        # description
        for description in response.css('#tabs .descriptionunit > p::text').extract():
            item['description'] = description.strip()

        # coordinates gps
        gps = re.findall("((\d+){1,3}\.(\d+?){15})", response.body)
        if gps and isinstance(gps, list):
            try:
                item['gps'] = {
                    'lat': gps[0][0],
                    'long': gps[1][0]
                }
            except IndexError as e:
                print("Can't split coords %s" % e)

        # features
        for li in response.css("#tabs-3 > div:nth-child(1) > ul:nth-child(2) li::text").extract():
            features.append(li)
            item['features'] = []
            item['features'] = features

        # detail page images
        item['file_urls'] = []
        for href in response.css('div.ad-thumbs a::attr("href")'):
            try:
                image_url = response.urljoin(href.extract())
                file_urls.append(image_url)
                item['file_urls'] = file_urls

            except BaseException:
                print("Can't extract href from detail page ad images")

        # push created item with all required fields
        items.update(item)

        # return
        yield items


    # enable custom file pipeline
    def get_media_requests(self, item, info):
        for url in item['file_urls']:
            yield scrapy.Request(url)

    # define item path after item download
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item