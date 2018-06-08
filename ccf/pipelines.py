# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ccf.data import CellItemStorage, PriceInputStorage,OilRelationStorage,MegMarketReportStorage,MegWeekReportStorage
from ccf.items import CellItem, PriceInput,OilRelationItem,MegMarketReportItem,MegWeekReportItem
from scrapy.utils.project import get_project_settings

class CcfPipeline(object):
    def process_item(self, item, spider):
        return item

class CellItemSave(object):
    def __init__(self):
        self.storage = CellItemStorage(get_project_settings().get('DATABASE'))
        
    def process_item(self, item, spider):
        if isinstance(item, CellItem):
            self.storage.save(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class PriceInputSave(object):
    def __init__(self):
        self.storage = PriceInputStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, PriceInput):
            if not self.storage.exist(item):
                self.storage.save(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class OilRelationSave(object):
    def __init__(self):
        self.storage = OilRelationStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, OilRelationItem):
            if not self.storage.exist(item):
                self.storage.save(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class MegMarketReportSave(object):
    def __init__(self):
        self.storage = MegMarketReportStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, MegMarketReportItem):
            if not self.storage.exist(item):
                self.storage.save(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item

class MegWeekReportSave(object):
    def __init__(self):
        self.storage = MegWeekReportStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, MegWeekReportItem):
            if not self.storage.exist(item):
                self.storage.save(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item
