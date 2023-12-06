# import scrapy


# class GdpSpider(scrapy.Spider):
#     name = "GDP"
#     allowed_domains = ["wikipedia.org"]
#     start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

#     def parse(self, response):
#         countries_table = response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")
#         print(len(response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")))
#         for country in countries_table :
#             country_name = country.xpath(".//td[1]/a/text()").get() # region = country.xpath(".//td[2]/a/text()").get()
#             forecast = country.xpath(".//td[3]/text()").get()
#             year = country.xpath(".//td[4]/text()").get()

#             yield {"country_name" : country_name , 
#                    "region" : region,
#                    "forecast" : forecast,
#                    "year" : year 
#             }

# import scrapy
# from countries_gdp.items import CountryGdpItem


# class GdpSpider(scrapy.Spider):
#     name = "GDP"
#     allowed_domains = ["wikipedia.org"]
#     start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

#     def parse(self, response):
#         countries_table = response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")
#         print(len(response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")))

#         for country in countries_table :
#             item = CountryGdpItem()

#             item["country_name"] = country.xpath(".//td[1]/a/text()").get()
#             item["region"] = country.xpath(".//td[2]/a/text()").get()
#             item["forecast"] = country.xpath(".//td[3]/text()").get()
#             item["year"] = country.xpath(".//td[4]/text()").get()


            
#             yield item


import scrapy
from countries_gdp.items import CountryGdpItem
from scrapy.loader import ItemLoader

class GdpSpider(scrapy.Spider):
    name = "GDP"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        countries_table = response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")

        # print(len(response.xpath("//table[contains(@class,'wikitable sortable')]/tbody/tr")))

        for country in countries_table :

            item = ItemLoader(item= CountryGdpItem() , selector= country)
            
            item.add_xpath("country_name", ".//td[1]/a")
            item.add_xpath("region", ".//td[2]/a")
            item.add_xpath("forecast", ".//td[3]")
            item.add_xpath("year", ".//td[4]")
                    
            
            yield item.load_item()


        

