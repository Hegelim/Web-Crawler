import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']

    # note that here you might need to change http to https
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        # countries is a list of selector objects
        for country in countries:
            # country name
            name = country.xpath(".//td[1]/a/text()").get()
            # get() extracts the textual data
            # getall() extracts the textual data as a list
            rate = country.xpath(".//td[2]/text()").get()
            yield {
                "country_name": name,
                "rate": rate
            }
