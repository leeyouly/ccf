# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LinkItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    
class CellItem(scrapy.Item):
    report_title    = scrapy.Field()
    report_date     = scrapy.Field()
    table_title     = scrapy.Field()
    index_name      = scrapy.Field()
    value_unit      = scrapy.Field()
    column_name     = scrapy.Field()
    column_value    = scrapy.Field()
    value_date      = scrapy.Field()

class PriceInput(scrapy.Item):
    product_name    = scrapy.Field()
    data_date       = scrapy.Field()
    ccf_price       = scrapy.Field()
    ccf_price2      = scrapy.Field()
    unit            = scrapy.Field()
    datetime_stamp  = scrapy.Field()
    datatype        = scrapy.Field()
