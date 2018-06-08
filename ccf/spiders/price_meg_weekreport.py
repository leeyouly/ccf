# -*- coding: utf-8 -*-
import scrapy
from ccf.items import MegWeekReportItem
import logging
import re
from ccf.table import table_to_list
import datetime
from dateutil.parser import parse
from scrapy.utils.project import get_project_settings

#CCF MEG市场周报 此爬虫只采集该页面的 “MEG华东港口库存情况(万吨)（完全统计） 部分” 其余部分在meg爬虫中
class PriceOilrelationSpider(scrapy.Spider):
    name = "price_meg_weekreport"
    allowed_domains = ["ccf.com.cn"]
    start_urls = (
        'http://www.ccf.com.cn/',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.ignore_page_incremental = True
        self.crawler.stats.set_value('spiderlog/source_name', u'中国化纤-MEG市场日报')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_CCF_MEG_WEEKREPORT'])
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
        # for page in range(1,389,1):
        for page in range(20,138,1):
            page_list_url = 'http://www.ccf.com.cn/newscenter/index.php?cur_row_pos=0&cur_pg_num='+str(page)+'&Class_ID=160000'
            request = scrapy.http.Request(page_list_url, callback = self.parse_page)
            yield request

    def parse_page(self,response):
        titleListHtml = response.xpath('/html/body/div[5]/div[2]/form/ul/li')
        for titleList in titleListHtml:
            titleURL = response.urljoin(titleList.xpath('./a/@href').extract()[0])
            titleName = titleList.xpath('./a/text()').extract()[0]
            if u'CCF MEG市场周报' in titleName:
                request = scrapy.http.Request(titleURL, callback=self.parse_content)
                yield request

    def parse_content(self, response):
        datadateHtml = response.xpath('/html/body/table[2]/tr/td[1]/table[2]/tr[4]/td/table/tr/td[1]/text()').extract()
        datadateStr = ''
        if datadateHtml <> []:
            datadateStr = datadateStr + datadateHtml[0]
            datadateNum = "".join(re.findall(r'\d+',datadateStr)) + '00'
            datadate = parse(datadateNum).strftime("%Y-%m-%d")
        else:
            print '------------------> datadate is null'
        data_table = response.xpath('//*[@id="newscontent"]/table[6]')
        if data_table == []:
            data_table = response.xpath('//*[@id="newscontent"]/table/tbody/tr[18]/td/table')
            if data_table == []:
                data_table = response.xpath('//*[@id="newscontent"]/table/tbody/tr[19]/td/table')
                if data_table <> []:
                    data_list = table_to_list(data_table)
                    if data_list[0][0] == u'产品':
                        for data in data_list[1:]:
                            item = MegWeekReportItem()
                            item['datadate'] = datadate
                            item['product_name'] = data[0]
                            item['last_week_value'] = data[1]
                            item['current_week_value'] = data[2]
                            item['update_dt'] = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
                            item['source'] = response.url
                            yield item
                    else:
                        print 'data_list[0][0] is not product ===============>' + response.url
                else:
                    print 'data_table is null 19------> ' + response.url
        else:
            data_list = table_to_list(data_table)
            if data_list[0][0] == u'产品':
                for data in data_list[1:]:
                    item = MegWeekReportItem()
                    item['datadate'] = datadate
                    item['product_name'] = data[0]
                    item['last_week_value'] = data[1]
                    item['current_week_value'] = data[2]
                    item['update_dt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    item['source'] = response.url
                    yield item
            else:
                print ' data_list[0][0] is not product  ------->' + response.url