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
                               
