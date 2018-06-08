# -*- coding:utf-8 -*-
from scrapy.http import HtmlResponse, Request
from ccf.spiders.pxdayxianhuo import pxdayxianhuo
import unittest
import os.path
import logging

class PxdayxianhuoTests(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pxdayxianhuo.html')
        f = open(data_file_path)
        html_content = f.read()	
        #print html_content
        f.close()
        report_title = u'亚洲PX市场日报（4.4）'
        request = Request(url='http://www.ccf.com.cn/newscenter/detail-410000-2016040500070.shtml', 
            meta={'report_title': report_title})
        response = HtmlResponse(url='http://www.ccf.com.cn/newscenter/detail-410000-2016041100028.shtml', body=html_content, request=request)
        spider = pxdayxianhuo()
        items = spider.parse_content(response)
        items = list(items)
        for item in items:
            logging.info('%(report_title)s\t%(report_date)s\t%(index_name)s\t%(column_name)s\t%(column_value)s' % item)
        self.assertEqual(len(items), 10)
            
        self.assertEqual(items[0]['report_title'], report_title)
        self.assertEqual(items[0]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[0]['index_name'], u'基准价')
        self.assertEqual(items[0]['column_name'], u'FOB韩国')
        self.assertEqual(items[0]['column_value'], '784.83-785.83*')

        self.assertEqual(items[1]['report_title'], report_title)
        self.assertEqual(items[1]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[1]['index_name'], u'基准价')
        self.assertEqual(items[1]['column_name'], u'CFR台湾/中国')
        self.assertEqual(items[1]['column_value'], '805.83-806.83*')

        self.assertEqual(items[2]['report_title'], report_title)
        self.assertEqual(items[2]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[2]['index_name'], u'四月下')
        self.assertEqual(items[2]['column_name'], u'FOB韩国')
        self.assertEqual(items[2]['column_value'], '785.00-787.00')
            
        self.assertEqual(items[3]['report_title'], report_title)
        self.assertEqual(items[3]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[3]['index_name'], u'四月下')
        self.assertEqual(items[3]['column_name'], u'CFR台湾/中国')
        self.assertEqual(items[3]['column_value'], '806.00-808.00')
        
        self.assertEqual(items[4]['report_title'], report_title)
        self.assertEqual(items[4]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[4]['index_name'], u'五月上')
        self.assertEqual(items[4]['column_name'], u'FOB韩国')
        self.assertEqual(items[4]['column_value'], '785.00-787.00')

        self.assertEqual(items[5]['report_title'], report_title)
        self.assertEqual(items[5]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[5]['index_name'], u'五月上')
        self.assertEqual(items[5]['column_name'], u'CFR台湾/中国')
        self.assertEqual(items[5]['column_value'], '806.00-808.00')
        
        self.assertEqual(items[6]['report_title'], report_title)
        self.assertEqual(items[6]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[6]['index_name'], u'五月下')
        self.assertEqual(items[6]['column_name'], u'FOB韩国')
        self.assertEqual(items[6]['column_value'], '785.00-787.00')

        self.assertEqual(items[7]['report_title'], report_title)
        self.assertEqual(items[7]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[7]['index_name'], u'五月下')
        self.assertEqual(items[7]['column_name'], u'CFR台湾/中国')
        self.assertEqual(items[7]['column_value'], u'806.00-808.00')
        
        self.assertEqual(items[8]['report_title'], report_title)
        self.assertEqual(items[8]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[8]['index_name'], u'六月上')
        self.assertEqual(items[8]['column_name'], u'FOB韩国')
        self.assertEqual(items[8]['column_value'], '783.00-785.00*')
        
        self.assertEqual(items[9]['report_title'], report_title)
        self.assertEqual(items[9]['report_date'], '2016-04-05 08:28:00')
        self.assertEqual(items[9]['index_name'], u'六月上')
        self.assertEqual(items[9]['column_name'], u'CFR台湾/中国')
        self.assertEqual(items[9]['column_value'], u'804.00-806.00*')
        
        
        