import scrapy

class LightSpider(scrapy.Spider):
    name = "light"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/izhevsk/category/svet"]

    def parse(self, response):
        lights = response.css("div._Ud0k")
        for light in lights:
            try:
                name = light.css('div.lsooF span::text').get()
                price = light.css('div.pY3d2 span::text').get()
                url = light.css('a').attrib['href']

                yield {
                    'name': name,
                    'price': price,
                    'url': url
                }

            except Exception as e:
                self.logger.error(f"ошибка {e}")