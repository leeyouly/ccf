# -*- coding: utf-8 -*-
import scrapy
from ccf.items import LinkItem, CellItem
import urlparse
import logging
import re
import datetime
from scrapy.utils.project import get_project_settings

class ZhifangdiduanSpider(scrapy.Spider):
    name = "zhifangdiduan"
    allowed_domains = ["www.ccf.com.cn"]
    start_urls = (
        'http://www.ccf.com.cn/',
    )
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'CCF-直纺涤短-市场周报')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CCF_REPORT_PRICE'])        
        login_url = 'http://www.ccf.com.cn/member/member.php'
        login_post_data = {
            'custlogin':    '1',
            'url':          'http://www.ccf.com.cn/newscenter/index.php?cur_row_pos=28',
            's':            '',
            'action':       'login',
            'username':     'kftz',
            'password':     'kf2014',
            'x':            '65',
            'y':            '7',
            }
        request = scrapy.http.FormRequest(url = login_url, 
            callback = self.login_callback, 
            formdata = login_post_data,
            )
        return [request]
    
    def login_callback(self, response):
        index_pages = (
            'http://www.ccf.com.cn/newscenter/list-160000.shtml',
        )
        page_count = 2
        index_pages = ['http://www.ccf.com.cn/newscenter/index.php?cur_row_pos=0&cur_pg_num=%s&Class_ID=160000' % i for i in range(1,page_count+1)]
        for index_page in index_pages:
            yield scrapy.http.Request(index_page, callback = self.parse_index_page)
        
    def parse_index_page(self, response):
        for link in response.css('ul.newslist li a'):
            link_title = link.xpath('./text()').extract_first()
            link_url = urlparse.urljoin(response.url, link.xpath('@href').extract_first())
            if u'CCF 直纺涤短市场周报' in link_title:
                item = LinkItem()
                item['title'] = link_title
                item['url'] = link_url
                yield scrapy.http.Request(link_url, callback=self.parse_content, meta={'report_title': link_title})
                
    def parse_content(self, response):
        report_date = self.extract_report_date(response)
        logging.debug(report_date)
        report_title = response.meta['report_title']
        logging.debug(report_title)
        # 2017-01-01 之后结构统一
        if response.css('td#fontzoom h2[class="lv_two_t"]'):
            table1 = response.css('td#fontzoom table[class="tb_2017v"]')[0]
            table2 = response.css('td#fontzoom table[class="tb_2017v"]')[1]
            table3 = response.css('td#fontzoom table[class="tb_2017v"]')[2]
        # 2017-01-01 之前
        elif response.css('td#fontzoom h1[class="weektitle"]'):
            table1 = response.css('td#fontzoom table[class="weektable"]')[0]
            table2 = response.css('td#fontzoom table[class="weektable"]')[1]
            table3 = response.css('td#fontzoom table[class="weektable"]')[2]
        else:
            table1 = response.css('table.zbtable')[0]
            table2 = response.css('table.zbtable')[1]
            table3 = response.css('table.zbtable')[2]

        for row in table1.xpath('./tbody/tr')[1:]:
            yield CellItem(
                report_title = report_title,
                report_date = report_date,
                table_title = u'CCF价格',
                index_name = ''.join(row.xpath('./td[1]//text()').extract()),
                value_unit = '',
                column_name = ''.join(table1.xpath('./tbody/tr[1]/td[3]//text()').extract()),
                column_value = ''.join(row.xpath('./td[3]//text()').extract()),
            )
        for row in table2.xpath('./tbody/tr')[1:]:
            yield CellItem(
                report_title = report_title,
                report_date = report_date,
                table_title = u'CCF指数',
                index_name = ''.join(row.xpath('./td[1]//text()').extract()),
                value_unit = '',
                column_name = ''.join(table2.xpath('./tbody/tr[1]/td[3]//text()').extract()),
                column_value = ''.join(row.xpath('./td[3]//text()').extract()),
            )
        for row in table3.xpath('./tbody/tr')[1:]:
            yield CellItem(
                report_title = report_title,
                report_date = report_date,
                table_title = u'相关产品价格',
                index_name = ''.join(row.xpath('./td[1]//text()').extract()),
                value_unit = '',
                column_name = ''.join(table3.xpath('./tbody/tr[1]/td[3]//text()').extract()),
                column_value = ''.join(row.xpath('./td[3]//text()').extract()),
            )
        
    def extract_report_date(self, response):
        p = re.compile(u'(\d+)年(\d+)月(\d+)日(\d+):(\d+)')
        for elem in response.css('td.px12t::text'):
            m = re.search(p, elem.extract())
            if m:
                report_date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))).strftime('%Y-%m-%d %H:%M:%S')
                return report_date
        
        
    def extract_items(self, report_title, report_date, table_title, rows):
        logging.debug(table_title)
