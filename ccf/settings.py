# -*- coding: utf-8 -*-


BOT_NAME = 'ccf'

SPIDER_MODULES = ['ccf.spiders']
NEWSPIDER_MODULE = 'ccf.spiders'

ITEM_PIPELINES = {
    'ccf.pipelines.CellItemSave': 300,
    'ccf.pipelines.PriceInputSave': 300,
    'ccf.pipelines.OilRelationSave': 300,
    'ccf.pipelines.MegMarketReportSave': 300,
    'ccf.pipelines.MegWeekReportSave': 300,
}
LOG_LEVEL = 'INFO'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
SPIDER_MIDDLEWARES = {
   # 'spiderlib.middlewares.IndexPageSaveMiddleware': 300,
}
EXTENSIONS = {
   'spiderlib.extensions.WriteEtlLog': 300,
}
DOWNLOAD_DELAY=3

DATABASE = 'oracle://stg:stg123@10.6.0.94:1521/?service_name=db'
USERNAME = 'kftz'
PASSWORD = 'kf2014'
