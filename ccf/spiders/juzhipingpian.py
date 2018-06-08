# -*- coding: utf-8 -*-
import scrapy
from ccf.items import LinkItem, CellItem
import urlparse
import logging
import re
import datetime
from scrapy.utils.project import get_project_settings

class JuzhipingpianSpider(scrapy.Spider):
    name = "juzhipingpian"
    allowed_domains = ["ccf.com.cn"]
    start_urls = (
        'http://www.ccf.com.cn/',
    )
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'CCF-聚酯瓶片-市场周报')
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
            if u'聚酯瓶片市场周报' in link_title:
                yield scrapy.http.Request(link_url, callback=self.parse_content, meta={'report_title': link_title})
                
    def parse_content(self, response):
        report_date = self.extract_report_date(response)
        report_title = response.meta['report_title']
        logging.debug(report_date)
        logging.debug(report_title)
        title_list = [
                u'周均价',
                u'合同原料成本（不包括加工成本）',
                u'合同原料成本（不包括加工成本)',
                u'现金流利润',
                u'现金流',
                u'周均负荷指数',
                u'其他出口市场报价',
                u'亚洲市场'
            ]
        
        if response.css('table.ar_table'):
            table1 = response.css('table.ar_table')[0]
            for row in table1.xpath('./tbody/tr')[1:]:
                yield CellItem(
                    report_title = report_title.strip(),
                    report_date = report_date,
                    table_title = u'周均价',
                    index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                    value_unit = '',
                    column_name = ''.join(table1.xpath('./tbody/tr[1]/td[4]//text()').extract()).strip(),
                    column_value = ''.join(row.xpath('./td[4]//text()').extract()).strip(),
                )
            
            table2 = response.css('table.ar_table')[1]
            for row in table2.xpath('./tbody/tr')[1:]:
                yield CellItem(
                    report_title = report_title.strip(),
                    report_date = report_date,
                    table_title = u'合同原料成本（不包括加工成本）',
                    index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                    value_unit = '',
                    column_name = ''.join(table2.xpath('./tbody/tr[1]/td[5]//text()').extract()).strip(),
                    column_value = ''.join(row.xpath('./td[5]//text()').extract()).strip(),
                )
            table3 = response.css('table.ar_table')[2]
            for row in table3.xpath('./tbody/tr')[1:]:
                yield CellItem(
                    report_title = report_title.strip(),
                    report_date = report_date,
                    table_title = u'现金流利润',
                    index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                    value_unit = '',
                    column_name = ''.join(table3.xpath('./tbody/tr[1]/td[4]//text()').extract()).strip(),
                    column_value = ''.join(row.xpath('./td[4]//text()').extract()).strip(),
                )
            table4 = response.css('table.ar_table')[3]
            for row in table4.xpath('./tbody/tr')[1:]:
                yield CellItem(
                    report_title = report_title.strip(),
                    report_date = report_date,
                    table_title = u'周均负荷指数',
                    index_name = ''.join(row.xpath('./td[1]//text()').extract()).strip(),
                    value_unit = '',
                    column_name = ''.join(table4.xpath('./tbody/tr[1]/td[4]//text()').extract()).strip(),
                    column_value = ''.join(row.xpath('./td[4]//text()').extract()).strip(),
                )
        # 2017-01-01 之后结构统一
        elif response.css('td#fontzoom h2[class="lv_two_t"]'):
            data_table = response.css('td#fontzoom div[id="newscontent"]')[0]
            for h2 in data_table.xpath('./h2'):
                table_title = u''.join(h2.xpath('.//text()').extract())
                table = h2.xpath('./following-sibling::*[1]')
                if table.css('table'):
                    temp_data_rows = [(tr, tr.xpath('./td'), ) for tr in table.xpath('.//tr')]
                    extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                    for item in extract_items:
                        yield item
                
        elif response.css('td#fontzoom table'):
            data_table = response.css('td#fontzoom table')[0]
            items = []
            temp_data_rows = []
            for tr in data_table.xpath('./tbody/tr'):
                if tr.xpath('./td[@colspan="5"]'):
                    # 把上一次查找到的title 和临时保存的rows 发送到extract_items()
                    if len(temp_data_rows)>0:
                        extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                        if extract_items:
                            items += extract_items
                    table_title = u''.join(tr.xpath('./td[@colspan="5"]//text()').extract())
                    logging.debug('table_title:%s' % table_title)
                    temp_data_rows = []
                    rowspan = 0
                    rowcounter = 0
                    continue
                elif u''.join(tr.xpath('./td[1]//text()').extract()) in title_list:
                    # 把上一次查找到的title 和临时保存的rows 发送到extract_items()
                    if len(temp_data_rows)>0:
                        extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                        if extract_items:
                            items += extract_items
                    table_title = u''.join(tr.xpath('./td[1]//text()').extract())
                    logging.debug('table_title:%s' % table_title)
                    temp_data_rows = []
                    rowspan = 0
                    rowcounter = 0
                    continue
                temp_data_rows.append((tr, tr.xpath('./td')))
            # 最后几行tr已经加入temp_data_rows的，还需要再提取一次
            if len(temp_data_rows)>0:
                extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                if extract_items:
                    items += extract_items
            for item in items:
                yield item
    
        
    def extract_report_date(self, response):
        p = re.compile(u'(\d+)年(\d+)月(\d+)日(\d+):(\d+)')
        for elem in response.css('td.px12t::text'):
            m = re.search(p, elem.extract())
            if m:
                report_date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))).strftime('%Y-%m-%d %H:%M:%S')
                return report_date
        
    def extract_row_cell_text(self, row, column_index):
        return ''.join(row[1][column_index].xpath('.//text()').extract())
        
    def extract_items(self, report_title, report_date, table_title, rows):
        if table_title == u'周均价':
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title.strip(),
                        table_title = table_title.strip(), 
                        index_name = self.extract_row_cell_text(row, 0).strip(),
                        value_unit = '',
                        column_name = self.extract_row_cell_text(rows[0], 3).strip(),
                        column_value = self.extract_row_cell_text(row,3).strip(),
                        report_date = report_date,
                    )
        elif table_title == u'合同原料成本（不包括加工成本）' or table_title == u'合同原料成本（不包括加工成本)':
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title.strip(),
                        table_title = table_title.strip(), 
                        index_name = self.extract_row_cell_text(row, 0).strip(),
                        value_unit = '',
                        column_name = self.extract_row_cell_text(rows[0], 4).strip(),
                        column_value = self.extract_row_cell_text(row,4).strip(),
                        report_date = report_date,
                    )
        elif table_title == u'现金流利润' or table_title == u'现金流':
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title.strip(),
                        table_title = table_title.strip(), 
                        index_name = self.extract_row_cell_text(row, 0).strip(),
                        value_unit = '',
                        column_name = self.extract_row_cell_text(rows[0], 3).strip(),
                        column_value = self.extract_row_cell_text(row,3).strip(),
                        report_date = report_date,
                    )
        elif table_title == u'周均负荷指数':
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title.strip(),
                        table_title = table_title.strip(), 
                        index_name = self.extract_row_cell_text(row, 0).strip(),
                        value_unit = '',
                        column_name = self.extract_row_cell_text(rows[0], 3).strip(),
                        column_value = self.extract_row_cell_text(row,3).strip(),
                        report_date = report_date,
                    )
        elif table_title == u'其他出口市场报价' or table_title == u'亚洲市场':
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title.strip(),
                        table_title = table_title.strip(), 
                        index_name = self.extract_row_cell_text(row, 0).strip(),
                        value_unit = '',
                        column_name = self.extract_row_cell_text(rows[0], 3).strip(),
                        column_value = self.extract_row_cell_text(row,3).strip(),
                        report_date = report_date,
                    )
