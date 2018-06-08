# -*- coding: utf-8 -*-
import scrapy
from ccf.items import PriceInput
import logging
import re
import datetime
from scrapy.utils.project import get_project_settings

class PriceNeipanptaSpider(scrapy.Spider):
    name = "price_neipanpta"
    allowed_domains = ["ccf.com.cn"]
    start_urls = (
        'http://www.ccf.com.cn/',
    )
    
    def start_requests(self):
        if datetime.datetime.now().hour < 19 or datetime.datetime.now().hour > 20:
            logging.info(u'每天19-20点进行抓取,正在退出')
            return
            
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.ignore_page_incremental = True
        self.crawler.stats.set_value('spiderlog/source_name', u'中国化纤-内盘PTA')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_CCF_PRICE_INPUT'])        
        login_url = 'http://www.ccf.com.cn/member/member.php'
        settings = get_project_settings()
        login_post_data = {
            'custlogin':    '1',
            'url':          'http://www.ccf.com.cn/newscenter/index.php?cur_row_pos=28',
            's':            '',
            'action':       'login',
            'username':     settings.get('USERNAME'),
            'password':     settings.get('PASSWORD'),
            'x':            '65',
            'y':            '7',
            }
        request = scrapy.http.FormRequest(url = login_url, 
            callback = self.login_callback, 
            formdata = login_post_data,
            )
        return [request]
    def login_callback(self, response):
        request = scrapy.http.Request('http://www.ccf.com.cn/dynamic_graph/getPrice.php?monitorId=3&type=dd',
            callback = self.parse_content)
        return [request]
     
    def parse_content(self, response):
        data_table = response.xpath('//div[@class="box_products_txt"]/table')[0]
        logging.debug(data_table)
        for row in data_table.xpath('./tr')[1:]:
            cells = row.xpath('./td')
            item = PriceInput()
            item['product_name'] = ''.join(cells[0].xpath('.//text()').extract()).strip()
            item['data_date'] = ''.join(cells[1].xpath('.//text()').extract()).strip()
            item['ccf_price'] = ''.join(cells[2].xpath('.//text()').extract()).strip()
            item['datetime_stamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item
