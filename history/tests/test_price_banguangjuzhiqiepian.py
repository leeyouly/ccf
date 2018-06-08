# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from ccf.spiders.price_banguangjuzhiqiepian import PriceBanguangjuzhiqiepianSpider
import os
import logging

class PriceBanguangjuzhiqiepianSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = PriceBanguangjuzhiqiepianSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/price_banguangjuzhiqiepian.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://www.ccf.com.cn/dynamic_graph/getPrice.php?monitorId=14&type=dd'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        items = list(items)
        self.assertEqual(len(items), 4)
        
        self.assertEqual(items[0]['product_name'],u'半光聚酯切片')
        self.assertEqual(items[0]['data_date'],u'2016/03/04')
        self.assertEqual(items[0]['ccf_price'],u'5725')
        self.assertEqual(items[1]['product_name'],u'半光聚酯切片')
        self.assertEqual(items[1]['data_date'],u'2016/03/03')
        self.assertEqual(items[1]['ccf_price'],u'5725')
        self.assertEqual(items[2]['product_name'],u'半光聚酯切片')
        self.assertEqual(items[2]['data_date'],u'2016/03/02')
        self.assertEqual(items[2]['ccf_price'],u'5700')
        self.assertEqual(items[3]['product_name'],u'半光聚酯切片')
        self.assertEqual(items[3]['data_date'],u'2016/03/01')
        self.assertEqual(items[3]['ccf_price'],u'5600')
