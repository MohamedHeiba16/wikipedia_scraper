# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3


class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["forecast"],float):
            raise DropItem("missing gdp value. item excluded")

        return item

class SaveToDatabasePipline:
    def __init__(self) -> None:
        self.con = sqlite3.connect("country_gdp.db")
        self.cur = self.con.cursor()

    def open_spider(self,spider):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS countries_gdp(country_name TEXT PRIMARY KEY,
                         region TEXT,
                         forecast REAL,
                         year INTEGER)""")
        self.con.commit()
    
    def process_item(self, item, spider):
        self.con.execute("""
                         INSERT INTO countries_gdp (country_name, region, forecast, year)VALUES (?,?,?,?)""",(item["country_name"],item["region"],item["forecast"],item["year"]))
        self.con.commit()
    
    def close_spider(self, spider):
        self.con.close()

class NoDuplicateCountryPipline:
    def __init__(self) -> None:
        self.country_dup = set()
    
    def process_item(self, item, spider):
        if item["country_name"] in self.country_dup:
            raise DropItem(f"Duplicate item found {item}")
        else:
            self.country_dup.add(item["country_name"])
            return item
        

        
        