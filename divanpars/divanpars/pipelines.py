import csv

class LightPipeline:
    def open_spider(self, light):
        self.file = open('light.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Наименование', 'Цена', 'Ссылка'])

    def close_spider(self, light):
        self.file.close()

    def process_item(self, item, light):
        self.writer.writerow([item['name'], item['price'], item['url']])
        return item