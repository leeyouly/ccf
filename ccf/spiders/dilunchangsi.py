# -*- coding: utf-8 -*-
import scrapy
from ccf.items import LinkItem, CellItem
import urlparse
import logging
import re
import datetime
from scrapy.utils.project import get_project_settings


class DilunchangsiSpider(scrapy.Spider):
    name = "dilunchangsi"
    allowed_domains = ["www.ccf.com.cn"]
    start_urls = (
        'http://www.ccf.com.cn/',
    )
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'CCF-涤纶长丝-市场周报')
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
            if u'涤纶长丝周报' in link_title:
                item = LinkItem()
                item['title'] = link_title
                item['url'] = link_url
                yield scrapy.http.Request(link_url, callback=self.parse_content, meta={'report_title': link_title})
                
    def parse_content(self, response):
        report_date = self.extract_report_date(response)
        data_table = response.css('td.newsviewtext > table')
        report_title = response.meta['report_title']
        temp_data_rows = []
        items = []
        # 2017-01-01 之后结构统一
        if response.css('td#fontzoom h2[class="lv_two_t"]'):
            data_table = response.css('td#fontzoom div[id="newscontent"]')[0]
            for h2 in data_table.xpath('./h2'):
                table_title = u''.join(h2.xpath('.//text()').extract())
                table = h2.xpath('./following-sibling::*[1]')
                if table.css('table'):
                    temp_data_rows = [(tr, tr.xpath('./td'), ) for tr in table.xpath('.//tr')]
                    extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                    if extract_items:
                        items += extract_items
        else:
            for tr in data_table.xpath('./tbody/tr'):
                if tr.xpath('./td[@colspan="6"]'):
                    # 把上一次查找到的title 和临时保存的rows 发送到extract_items()
                    if len(temp_data_rows)>0:
                        extract_items = self.extract_items(report_title, report_date, table_title, temp_data_rows)
                        if extract_items:
                            items += extract_items
                    #print tr.xpath('./td[@colspan="6"]//text()').extract()
                    table_title = u''.join(tr.xpath('./td[@colspan="6"]//text()').extract())
                    temp_data_rows = []
                    rowspan = 0
                    rowcounter = 0
                    continue
                
                temp_data_rows.append((tr, tr.xpath('./td')))
        return items
        
    def normalize_rows(self, rows):
        '''
            rows as (Selector('TR'), [Selector['TD']] format
        '''
        row_counter = 0
        current_rowspan = 1
        tmp_rowspaned_cell = None
        for row in rows:
            row_counter += 1 

            if row[1][0].xpath('./@rowspan'):
                current_rowspan = int(row[1][0].xpath('./@rowspan').extract_first())
                tmp_rowspaned_cell = row[1][0]
                row_counter = 0
                continue 
                
            if current_rowspan > row_counter and tmp_rowspaned_cell:
                row[1].insert(0, tmp_rowspaned_cell)
        return rows
    
    def extract_report_date(self, response):
        p = re.compile(u'(\d+)年(\d+)月(\d+)日(\d+):(\d+)')
        for elem in response.css('td.px12t::text'):
            m = re.search(p, elem.extract())
            if m:
                report_date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))).strftime('%Y-%m-%d %H:%M:%S')
                return report_date
        
    
    def extract_cell_text(self, rows, row_index, column_index):
        return ''.join(rows[row_index].xpath('./td[' + str(column_index+1) + ']//text()').extract())
    
    def extract_row_cell_text(self, row, column_index):
        return ''.join(row[1][column_index].xpath('.//text()').extract())
        
    def print_row(self, row):
        print ''
        for cell in row[1]:
            print ''.join(cell.xpath('.//text()').extract()),
    
    def extract_items(self, report_title, report_date, table_title, rows):
        if table_title == u'CCF价格指数':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        value_unit = self.extract_row_cell_text(row, 1),
                        column_name = self.extract_row_cell_text(rows[0], 4),
                        column_value = self.extract_row_cell_text(row,4),
                        report_date = report_date,
                    )
        if table_title == u'CCF聚酯原料价格':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = u'聚酯原料价格',
                        value_unit = self.extract_row_cell_text(row, 0),
                        column_name = self.extract_row_cell_text(rows[0], 3),
                        column_value = self.extract_row_cell_text(row,3),
                        report_date = report_date,
                    )
        if table_title == u'涤丝价格（内盘）' or table_title == u'CCF涤丝价格（内盘）':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        value_unit = self.extract_row_cell_text(row, 1),
                        column_name = self.extract_row_cell_text(rows[0], 4),
                        column_value = self.extract_row_cell_text(row,4),
                        report_date = report_date,
                    )
        if table_title == u'涤丝价格（外盘）' or table_title == u'CCF涤丝价格（外盘）':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        value_unit = self.extract_row_cell_text(row, 1),
                        column_name = self.extract_row_cell_text(rows[0], 4),
                        column_value = self.extract_row_cell_text(row,4),
                        report_date = report_date,
                    )
        if table_title == u'现金流状况':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        value_unit = self.extract_row_cell_text(row, 1),
                        column_name = self.extract_row_cell_text(rows[0], 4),
                        column_value = self.extract_row_cell_text(row,4),
                        report_date = report_date,
                    )
        if table_title == u'涤丝现金流状况':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = u'江浙市场',
                        value_unit = self.extract_row_cell_text(row, 0),
                        column_name = self.extract_row_cell_text(rows[0], 3),
                        column_value = self.extract_row_cell_text(row,3),
                        report_date = report_date,
                    )
        if table_title == u'CCF负荷指数':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        column_name = self.extract_row_cell_text(rows[0], 3),
                        column_value = self.extract_row_cell_text(row,3),
                        report_date = report_date,
                    )
        if table_title == u'CCF 库存指数':
            rows = self.normalize_rows(rows)
            for row in rows[1:]:
                yield CellItem(
                        report_title = report_title,
                        table_title = table_title, 
                        index_name = self.extract_row_cell_text(row, 0),
                        value_unit = self.extract_row_cell_text(row, 1),
                        column_name = self.extract_row_cell_text(rows[0], 4),
                        column_value = self.extract_row_cell_text(row,4),
                        report_date = report_date,
                    )
        
