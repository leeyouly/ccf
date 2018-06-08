import PyDB
import urlparse
from spiderlib.data import DataStorage


class CellItemStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 't_ec_ccf_report_price'
        self.db.set_metadata(self.table_name, [
                                PyDB.StringField('report_title', is_key=True),
                                PyDB.DateField("report_date", is_key=True),
                                PyDB.StringField('table_title', is_key=True),
                                PyDB.StringField('index_name', is_key=True),
                                PyDB.StringField('column_name', is_key=True),
                                PyDB.StringField('value_unit'),
                                PyDB.StringField('column_value'),
                                PyDB.StringField('value_date'),
                               ])
                               
class PriceInputStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_CCF_PRICE_INPUT'
        self.db.set_metadata(self.table_name, [
                                PyDB.StringField('product_name', is_key=True),
                                PyDB.StringField("data_date", is_key=True),
                                PyDB.StringField('ccf_price'),
                                PyDB.StringField('ccf_price2'),
                                PyDB.StringField('unit'),
                                PyDB.StringField('datetime_stamp'),
                                PyDB.StringField('datatype'),
                               ])


class OilRelationStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CCF_OIL_RELATION'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField('datadate', is_key=True),
            PyDB.StringField('product_name', is_key=True),
            PyDB.StringField("market", is_key=True),
            PyDB.StringField('lastday_price'),
            PyDB.StringField('currentday_price'),
            PyDB.StringField('change_price'),
            PyDB.StringField('unit'),
            PyDB.DatetimeField('update_dt'),
            PyDB.StringField('source'),
        ])

class MegMarketReportStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CCF_MEG_MARKETREPORT'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField('datadate', is_key=True),
            PyDB.StringField('product_name', is_key=True),
            PyDB.StringField("day_avg_price"),
            PyDB.StringField('change_price'),
            PyDB.DatetimeField('update_dt'),
            PyDB.StringField('source'),
        ])

class MegWeekReportStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CCF_MEG_WEEKREPORT'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField('datadate', is_key=True),
            PyDB.StringField('product_name', is_key=True),
            PyDB.StringField("last_week_value"),
            PyDB.StringField('current_week_value'),
            PyDB.DatetimeField('update_dt'),
            PyDB.StringField('source'),
        ])