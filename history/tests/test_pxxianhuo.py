# -*- coding:utf8 -*-
from scrapy.http import HtmlResponse
from ccf.spiders.pxxianhuo import PxxianhuoSpider
import unittest
import os.path
import logging

class PXXianhuoTests(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pxxianhuo.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        response = HtmlResponse(url='', body=html_content)
        spider = PxxianhuoSpider()
        items = list(spider.parse_content(response))
        
        report_title = u'亚洲PX现货市场周报（1.18-1.22)'
        report_date = '2016-01-22 14:12:00'
        
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0]['index_name'] , u'PX月均价（CFR美元/吨）')
        self.assertEqual(items[0]['column_name'] , u'2016年1月')
        self.assertEqual(items[0]['column_value'] , u'720（截止21日）')
        self.assertEqual(items[0]['report_date'] , report_date)
        self.assertEqual(items[0]['report_title'] , report_title)
        self.assertEqual(items[0]['table_title'] , u'合同价格')
        
        self.assertEqual(items[1]['index_name'] , u'国内大厂合约（元/吨）')
        self.assertEqual(items[1]['column_name'] , u'2016年1月')
        self.assertEqual(items[1]['column_value'] , u'5690')
        self.assertEqual(items[1]['report_date'] , report_date)
        self.assertEqual(items[1]['report_title'] , report_title)
        self.assertEqual(items[1]['table_title'] , u'合同价格')
        
        self.assertEqual(items[2]['index_name'] , u'PX进口量（万吨）')
        self.assertEqual(items[2]['column_name'] , u'2016年1月')
        self.assertEqual(items[2]['column_value'] , u'')
        self.assertEqual(items[2]['report_date'] , report_date)
        self.assertEqual(items[2]['report_title'] , report_title)
        self.assertEqual(items[2]['table_title'] , u'合同价格')
            
        self.assertEqual(items[3]['index_name'] , u'中国PX')
        self.assertEqual(items[3]['column_name'] , u'1月22日')
        self.assertEqual(items[3]['column_value'] , u'60')
        self.assertEqual(items[3]['report_date'] , report_date)
        self.assertEqual(items[3]['report_title'] , report_title)
        self.assertEqual(items[3]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[4]['index_name'] , u'亚洲PX')
        self.assertEqual(items[4]['column_name'] , u'1月22日')
        self.assertEqual(items[4]['column_value'] , u'73.4')
        self.assertEqual(items[4]['report_date'] , report_date)
        self.assertEqual(items[4]['report_title'] , report_title)
        self.assertEqual(items[4]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[5]['index_name'] , u'中国PTA')
        self.assertEqual(items[5]['column_name'] , u'1月22日')
        self.assertEqual(items[5]['column_value'] , u'65.1')
        self.assertEqual(items[5]['report_date'] , report_date)
        self.assertEqual(items[5]['report_title'] , report_title)
        self.assertEqual(items[5]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[6]['index_name'] , u'中国聚酯')
        self.assertEqual(items[6]['column_name'] , u'1月22日')
        self.assertEqual(items[6]['column_value'] , u'68.4')
        self.assertEqual(items[6]['report_date'] , report_date)
        self.assertEqual(items[6]['report_title'] , report_title)
        self.assertEqual(items[6]['table_title'] , u'负荷指数')
            
    def test_parse2(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/pxxianhuo2.html')
        f = open(data_file_path)
        html_content = f.read()
        #print html_content
        f.close()
        response = HtmlResponse(url='', body=html_content)
        spider = PxxianhuoSpider()
        items = list(spider.parse_content(response))
        
        report_date = '2015-04-30 13:13:00'
        report_title = u'亚洲PX现货市场周报（4.27-4.30）'
        
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0]['index_name'] , u'PX月均价（CFR美元/吨）')
        self.assertEqual(items[0]['column_name'] , u'2015年5月')
        self.assertEqual(items[0]['column_value'] , u'')
        self.assertEqual(items[0]['report_date'] , report_date)
        self.assertEqual(items[0]['report_title'] , report_title)
        self.assertEqual(items[0]['table_title'] , u'合同价格')
        
        self.assertEqual(items[1]['index_name'] , u'中石化合约（元/吨）')
        self.assertEqual(items[1]['column_name'] , u'2015年5月')
        self.assertEqual(items[1]['column_value'] , u'7100报')
        self.assertEqual(items[1]['report_date'] , report_date)
        self.assertEqual(items[1]['report_title'] , report_title)
        self.assertEqual(items[1]['table_title'] , u'合同价格')
        
        self.assertEqual(items[2]['index_name'] , u'PX进口量（万吨）')
        self.assertEqual(items[2]['column_name'] , u'2015年5月')
        self.assertEqual(items[2]['column_value'] , u'')
        self.assertEqual(items[2]['report_date'] , report_date)
        self.assertEqual(items[2]['report_title'] , report_title)
        self.assertEqual(items[2]['table_title'] , u'合同价格')
        
        self.assertEqual(items[3]['index_name'] , u'中国PX')
        self.assertEqual(items[3]['column_name'] , u'4月30日')
        self.assertEqual(items[3]['column_value'] , u'67.5')
        self.assertEqual(items[3]['report_date'] , report_date)
        self.assertEqual(items[3]['report_title'] , report_title)
        self.assertEqual(items[3]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[4]['index_name'] , u'亚洲PX')
        self.assertEqual(items[4]['column_name'] , u'4月30日')
        self.assertEqual(items[4]['column_value'] , u'68.6')
        self.assertEqual(items[4]['report_date'] , report_date)
        self.assertEqual(items[4]['report_title'] , report_title)
        self.assertEqual(items[4]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[5]['index_name'] , u'PTA')
        self.assertEqual(items[5]['column_name'] , u'4月30日')
        self.assertEqual(items[5]['column_value'] , u'67.6')
        self.assertEqual(items[5]['report_date'] , report_date)
        self.assertEqual(items[5]['report_title'] , report_title)
        self.assertEqual(items[5]['table_title'] , u'负荷指数')
        
        self.assertEqual(items[6]['index_name'] , u'聚酯')
        self.assertEqual(items[6]['column_name'] , u'4月30日')
        self.assertEqual(items[6]['column_value'] , u'84.7')
        self.assertEqual(items[6]['report_date'] , report_date)
        self.assertEqual(items[6]['report_title'] , report_title)
        self.assertEqual(items[6]['table_title'] , u'负荷指数')