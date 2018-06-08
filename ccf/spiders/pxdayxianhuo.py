 #-*- coding: utf-8 -*-
import scrapy
import urlparse
import logging
from ccf.items import LinkItem, CellItem
from scrapy.utils.project import get_project_settings
import re
import datetime

class pxdayxianhuo(scrapy.Spider):
    name = "pxdayxianhuo"
    allowed_domains = ['ccf.com.cn']
    start_urls = (
        'http://ccf.com.cn/',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'CCF-PX现货-市场日报')
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
        return request
    
    def login_callback(self, response):
        index_pages = (
            'http://www.ccf.com.cn/newscenter/index.php?Class_ID=410000',
        )
        page_count = 2
        index_pages = ['http://www.ccf.com.cn/newscenter/index.php?cur_row_pos=28&cur_pg_num=%s&Class_ID=410000' % i for i in range(1,page_count+1)]
        for index_page in index_pages:
            yield scrapy.http.Request(index_page, callback = self.parse_index_page)
        
    def parse_index_page(self, response):
        for link in response.css('ul.newslist li a'):
            link_title = link.xpath('./text()').extract_first().strip()
            link_url = urlparse.urljoin(response.url, link.xpath('@href').extract_first())
            if link_title and (u'亚洲PX市场日报' in link_title):
                yield scrapy.http.Request(link_url, callback=self.parse_content, meta={'report_title': link_title})
    
    def extract_report_date(self, response):
        p = re.compile(u'(\d+)年(\d+)月(\d+)日(\d+):(\d+)')
        for elem in response.css('td.px12t::text'):
            m = re.search(p, elem.extract())
            if m:
                report_date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))).strftime('%Y-%m-%d %H:%M:%S')
                return report_date
        
    
    def parse_content(self, response):
        report_title = response.meta['report_title']
        report_date = self.extract_report_date(response)
        logging.debug(report_date)
        logging.debug(report_title)
        table1 = response.css('td#fontzoom table')[0]
        seq = 1
        for row in table1.xpath('./tbody/tr')[2:]:
            yield CellItem(
                        report_title = report_title,
                        index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                        column_name = ''.join(table1.xpath('./tbody/tr[1]/td[2]//text()').extract()).strip(),
                        column_value = ''.join(row.xpath('./td[2]//text()').extract()).strip(),
                        report_date = report_date,
                        value_date = report_date,
                        table_title = str(seq),
                    )
            yield CellItem(
                        report_title = report_title,
                        index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                        column_name = ''.join(table1.xpath('./tbody/tr[1]/td[4]//text()').extract()).strip(),
                        column_value = ''.join(row.xpath('./td[4]//text()').extract()).strip(),
                        report_date = report_date,
                        value_date = report_date,
                        table_title = str(seq),
                     )
            seq += 1
       