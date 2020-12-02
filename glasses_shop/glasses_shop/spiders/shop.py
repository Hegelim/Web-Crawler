import scrapy


class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        glasses_products = response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for glasses in glasses_products:
            product_title = glasses.xpath(".//div[@class='p-title']/a/@title").get()
            price = glasses.xpath(".//div[@class='p-price']//span/text()").get()
            image_url = glasses.xpath(".//div[@class='product-img-outer']//img[@class='lazy d-block w-100 product-img-default']/@data-src").get()
            product_url = glasses.xpath(".//div[@class='product-img-outer']/a/@href").get()
            yield {
                "product_name": product_title,
                "price": price,
                "image_url": image_url,
                "product_url": product_url
            }

        next_page = response.xpath("//a[@rel='next']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

