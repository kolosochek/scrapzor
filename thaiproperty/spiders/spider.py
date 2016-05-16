# -*- coding: utf-8 -*-
# made by megusta
# sample spider for thaiproperty.com
# TODO: add watermark replacement using PIL
from scrapy import Spider, Request
from re import findall
from thaiproperty.items import ThaipropertyItem
from hashlib import md5
from scrapy.exceptions import DropItem

class ThaipropertySpider(Spider):
    name = "thaipropertycom_spider"
    start_urls = ["http://www.thaiproperty.com"]
    page_counter = 0
    max_page = 0
    site_sections = [
        "http://www.thaiproperty.com/for_rent/condos.html?&per_page=",
        "http://www.thaiproperty.com/for_rent/houses.html?&per_page=",
        "http://www.thaiproperty.com/for_sale/condos.html?&per_page=",
        "http://www.thaiproperty.com/for_sale/houses.html?&per_page="]

    # __init__()
    def parse(self, response):
        for page in self.site_sections:
            yield Request(page, self.parse_section)

    # go onto section page(i.e. condos for sale) and then iterate sections and work on each section going deeper
    # from sections to caregory page and then to the detail ad page
    def parse_section(self, response):
        for max_page in response.css('p.p-box-paging:nth-child(1) > span:nth-child(3)::text').extract():
            try:
                page = max_page.replace(',', '')
                try:
                    page = findall('(\d+)', page)[::-1][0]
                    self.max_page = int(page)
                except BaseException:
                    print("Can't get max_page: something broken")
            except TypeError:
                print("Can't convert max_page value to int")
        if isinstance(self.max_page, int) and self.max_page > 0 and self.page_counter < self.max_page:
            while(self.page_counter <= self.max_page):
                url = "%s%s" % (response.url, self.page_counter)
                # switching pages
                self.page_counter += 20
                yield Request(url, self.parse_pages)


    # get links from category page and make request on each one of it
    def parse_pages(self, response):
        for href in response.css('.subBoxDetailList > a::attr("href")'):
            full_url = response.urljoin(href.extract())
            yield Request(full_url, self.parse_ad)

    # scrap the detail ad page
    def parse_ad(self, response):
        file_urls = []
        features = []
        items = {}
        # create Item object and fill it down
        item = ThaipropertyItem()

        # url
        item['url'] = response.url

        # category
        if u'/for_rent/' in response.url:
            item['category'] = 'for_rent'
        elif u'/for_sale/' in response.url:
            item['category'] = 'for_sale'
        else:
            item['category'] = False

        # type
        if u"/condos.html" in response.url or u"/condos/" in response.url:
            item['type'] = 'condominimum'
        elif u"/houses.html" in response.url or u"/houses/" in response.url:
            item['type'] = 'house'
        else:
            item['type'] = False

        # hash
        item['hash'] = md5(response.url).hexdigest()

        # isRented
        item['isRented'] = False
        for rented in response.css('.rentedunti::text').extract():
            if u'Rented Until' in rented:
                item['isRented'] = True

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

        # all prices are in Thai Baht(b), but you can scrap prices in USD or RUR for example
        # rent price by month
        for month_rent_price in response.css("span#boxpriceShow2::text").extract():
            item['price_rent'] = month_rent_price.replace(u'\u0e3f', '').replace(' /m', '').replace(',', '') # replace baht currency sign

        # sale price by month
        for sale_price in response.css("#boxpriceShow::text").extract():
            item['price_sale'] = sale_price.replace(u'\u0e3f', '').replace(',', '') # replace baht currency sign

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
        gps = findall("((\d+){1,3}\.(\d+?){15})", response.body)
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
        item['file_urls'] = []
        for url in item['file_urls']:
            yield Request(url)

    # define item path after item download
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item