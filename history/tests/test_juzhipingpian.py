# -*- coding:utf-8 -*-
from scrapy.http import HtmlResponse, Request
from ccf.spiders.juzhipingpian import JuzhipingpianSpider
import unittest
import os.path
import logging

class ZhifangdiduanTests(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'juzhipingpian.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        report_title = u'CCF 聚酯瓶片市场周报（1.11-1.15）'
        request = Request(url='http://www.ccf.com.cn/newscenter/detail-160000-2016011500379.shtml', 
            meta={'report_title': report_title})
        response = HtmlResponse(url='http://www.ccf.com.cn/newscenter/detail-160000-2016011500379.shtml', body=html_content, request=request)
        spider = JuzhipingpianSpider()
        items = spider.parse_content(response)
        items = list(items)
        for item in items:
            logging.info('%(report_title)s\t%(table_title)s\t%(report_date)s\t%(index_name)s\t%(column_name)s\t%(column_value)s' % item)
            
        self.assertEqual(items[0]['report_title'], report_title)
        self.assertEqual(items[0]['table_title'], u'周均价')
        self.assertEqual(items[0]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[0]['index_name'], u'碳酸片(元/吨)')
        self.assertEqual(items[0]['column_name'], '1.11-1.15')
        self.assertEqual(items[0]['column_value'], '5908')
        
        self.assertEqual(items[1]['report_title'], report_title)
        self.assertEqual(items[1]['table_title'], u'周均价')
        self.assertEqual(items[1]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[1]['index_name'], u'热罐片(元/吨)')
        self.assertEqual(items[1]['column_name'], '1.11-1.15')
        self.assertEqual(items[1]['column_value'], '5808')
        
        self.assertEqual(items[2]['report_title'], report_title)
        self.assertEqual(items[2]['table_title'], u'周均价')
        self.assertEqual(items[2]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[2]['index_name'], u'内盘水瓶片(元/吨)')
        self.assertEqual(items[2]['column_name'], '1.11-1.15')
        self.assertEqual(items[2]['column_value'], '5808')
        
        self.assertEqual(items[3]['report_title'], report_title)
        self.assertEqual(items[3]['table_title'], u'周均价')
        self.assertEqual(items[3]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[3]['index_name'], u'外盘水瓶片(美元/吨)')
        self.assertEqual(items[3]['column_name'], '1.11-1.15')
        self.assertEqual(items[3]['column_value'], '791')
        
        self.assertEqual(items[4]['report_title'], report_title)
        self.assertEqual(items[4]['table_title'], u'合同原料成本（不包括加工成本）')
        self.assertEqual(items[4]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[4]['index_name'], u'聚酯原料')
        self.assertEqual(items[4]['column_name'], u'2015年12月')
        self.assertEqual(items[4]['column_value'], '5485.7')
        
        self.assertEqual(items[5]['report_title'], report_title)
        self.assertEqual(items[5]['table_title'], u'现金流利润')
        self.assertEqual(items[5]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[5]['index_name'], u'内盘(元/吨)')
        self.assertEqual(items[5]['column_name'], u'1月14日')
        self.assertEqual(items[5]['column_value'], '76.2')
        
        self.assertEqual(items[6]['report_title'], report_title)
        self.assertEqual(items[6]['table_title'], u'现金流利润')
        self.assertEqual(items[6]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[6]['index_name'], u'出口(美元/吨)')
        self.assertEqual(items[6]['column_name'], u'1月14日')
        self.assertEqual(items[6]['column_value'], '15.68')
        
        self.assertEqual(items[7]['report_title'], report_title)
        self.assertEqual(items[7]['table_title'], u'周均负荷指数')
        self.assertEqual(items[7]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[7]['index_name'], u'开机率')
        self.assertEqual(items[7]['column_name'], u'1.11-1.15')
        self.assertEqual(items[7]['column_value'], '72.7%')
        
        self.assertEqual(items[8]['report_title'], report_title)
        self.assertEqual(items[8]['table_title'], u'周均负荷指数')
        self.assertEqual(items[8]['report_date'], '2016-01-15 15:01:00')
        self.assertEqual(items[8]['index_name'], u'库存')
        self.assertEqual(items[8]['column_name'], u'1.11-1.15')
        self.assertEqual(items[8]['column_value'], u'正常')
        
        
        
    def test_parse2(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'juzhipingpian2.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        page_url = 'http://www.ccf.com.cn/newscenter/detail-160000-2016012900425.shtml'
        report_title = u'CCF 聚酯瓶片市场周报（1.25-1.29）'
        request = Request(page_url, 
            meta={'report_title': report_title})
        response = HtmlResponse(url=page_url, body=html_content, request=request)
        spider = JuzhipingpianSpider()
        items = spider.parse_content(response)
        items = list(items)
        for item in items:
            logging.info('%(report_title)s\t%(table_title)s\t%(report_date)s\t%(index_name)s\t%(column_name)s\t%(column_value)s' % item)
            
        self.assertEqual(items[0]['report_title'], report_title)
        self.assertEqual(items[0]['table_title'], u'周均价')
        self.assertEqual(items[0]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[0]['index_name'], u'碳酸片(元/吨)')
        self.assertEqual(items[0]['column_name'], '1.25-1.29')
        self.assertEqual(items[0]['column_value'], '5995')
        
        self.assertEqual(items[1]['report_title'], report_title)
        self.assertEqual(items[1]['table_title'], u'周均价')
        self.assertEqual(items[1]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[1]['index_name'], u'热罐片(元/吨)')
        self.assertEqual(items[1]['column_name'], '1.25-1.29')
        self.assertEqual(items[1]['column_value'], '5895')
        
        self.assertEqual(items[2]['report_title'], report_title)
        self.assertEqual(items[2]['table_title'], u'周均价')
        self.assertEqual(items[2]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[2]['index_name'], u'内盘水瓶片(元/吨)')
        self.assertEqual(items[2]['column_name'], '1.25-1.29')
        self.assertEqual(items[2]['column_value'], '5895')
        
        self.assertEqual(items[3]['report_title'], report_title)
        self.assertEqual(items[3]['table_title'], u'周均价')
        self.assertEqual(items[3]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[3]['index_name'], u'出口水瓶片(美元/吨)')
        self.assertEqual(items[3]['column_name'], '1.25-1.29')
        self.assertEqual(items[3]['column_value'], '778')
        
        
        self.assertEqual(items[4]['report_title'], report_title)
        self.assertEqual(items[4]['table_title'], u'其他出口市场报价')
        self.assertEqual(items[4]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[4]['index_name'], u'印度(FOB美元/吨)')
        self.assertEqual(items[4]['column_name'], '1.25-1.29')
        self.assertEqual(items[4]['column_value'], '740-780')
        
        self.assertEqual(items[5]['report_title'], report_title)
        self.assertEqual(items[5]['table_title'], u'其他出口市场报价')
        self.assertEqual(items[5]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[5]['index_name'], u'韩国(FOB美元/吨)')
        self.assertEqual(items[5]['column_name'], '1.25-1.29')
        self.assertEqual(items[5]['column_value'], '810-830')
        
        self.assertEqual(items[6]['report_title'], report_title)
        self.assertEqual(items[6]['table_title'], u'其他出口市场报价')
        self.assertEqual(items[6]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[6]['index_name'], u'东南亚(FOB美元/吨)')
        self.assertEqual(items[6]['column_name'], '1.25-1.29')
        self.assertEqual(items[6]['column_value'], '810-850')
        
        self.assertEqual(items[7]['report_title'], report_title)
        self.assertEqual(items[7]['table_title'], u'合同原料成本（不包括加工成本）')
        self.assertEqual(items[7]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[7]['index_name'], u'聚酯原料')
        self.assertEqual(items[7]['column_name'], u'2016年1月')
        self.assertEqual(items[7]['column_value'], '5382')
        
        
        self.assertEqual(items[8]['report_title'], report_title)
        self.assertEqual(items[8]['table_title'], u'现金流利润')
        self.assertEqual(items[8]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[8]['index_name'], u'内盘(元/吨)')
        self.assertEqual(items[8]['column_name'], u'1月28日')
        self.assertEqual(items[8]['column_value'], '7.1')
        
        
        self.assertEqual(items[9]['report_title'], report_title)
        self.assertEqual(items[9]['table_title'], u'现金流利润')
        self.assertEqual(items[9]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[9]['index_name'], u'出口(美元/吨)')
        self.assertEqual(items[9]['column_name'], u'1月28日')
        self.assertEqual(items[9]['column_value'], '-4.3')
        
        self.assertEqual(items[10]['report_title'], report_title)
        self.assertEqual(items[10]['table_title'], u'周均负荷指数')
        self.assertEqual(items[10]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[10]['index_name'], u'开机率')
        self.assertEqual(items[10]['column_name'], u'1.18-1.22')
        self.assertEqual(items[10]['column_value'], '81.60%')
        
        self.assertEqual(items[11]['report_title'], report_title)
        self.assertEqual(items[11]['table_title'], u'周均负荷指数')
        self.assertEqual(items[11]['report_date'], '2016-01-29 15:15:00')
        self.assertEqual(items[11]['index_name'], u'库存')
        self.assertEqual(items[11]['column_name'], u'1.18-1.22')
        self.assertEqual(items[11]['column_value'], u'正常')
        
        
    