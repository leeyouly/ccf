# -*- coding:utf8 -*-
from scrapy.http import HtmlResponse
from ccf.spiders.dilunchangsi import DilunchangsiSpider
import unittest
import os.path
import scrapy

class DilunChangsiTests(unittest.TestCase):
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'dilunchangsi.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://www.ccf.com.cn/newscenter/detail-160000-2016030400473.shtml'
        request = scrapy.http.Request(url=page_url, meta={'report_title':'CCF ABS市场周报(2.29-3.4)'})
        response = HtmlResponse(url='', request=request, body=html_content) 
        spider = DilunchangsiSpider()
        spider.parse_content(response)



        
        
        
        
        
        
