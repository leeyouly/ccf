# -*- coding:utf-8 -*-
from scrapy.http import HtmlResponse, Request
from ccf.spiders.zhifangdiduan import ZhifangdiduanSpider
import unittest
import os.path
import logging

class ZhifangdiduanTests(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'zhifangdiduan.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        report_title = u'CCF 直纺涤短市场周报（1.18-1.22）'
        request = Request(url='http://www.ccf.com.cn/newscenter/detail-160000-2016012200474.shtml', 
            meta={'report_title': report_title})
        response = HtmlResponse(url='', body=html_content, request=request)
        spider = ZhifangdiduanSpider()
        items = spider.parse_content(response)
        for item in items:
            logging.info('%(report_title)s\t%(table_title)s\t%(report_date)s\t%(index_name)s\t%(column_name)s\t%(column_value)s' % item)
            
            
    def test_parse2(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'zhifangdiduan2.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        report_title = u'CCF 直纺涤短市场周报（1.11-1.15）'
        request = Request(url='http://www.ccf.com.cn/newscenter/detail-160000-2016012200474.shtml', 
            meta={'report_title': report_title})
        response = HtmlResponse(url='', body=html_content, request=request)
        spider = ZhifangdiduanSpider()
        items = spider.parse_content(response)
        for item in items:
            logging.info('%(report_title)s\t%(table_title)s\t%(report_date)s\t%(index_name)s\t%(column_name)s\t%(column_value)s' % item)
            