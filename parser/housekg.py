import requests
from parsel import Selector
from pprint import pprint
from db.queries import init_db, parser_db, create_table
from aiogram import Router


class HousekgScraper:
    MAIN_URL = 'https://www.house.kg/snyat'
    def get_html(self):
        response = requests.get(self.MAIN_URL)
        print(response.status_code)
        if response.status_code == 200:
            return response.text

    # def get_title(self, html):
    #     selector = Selector(text=html)
    #     title = selector.css('title::text').get()
    #     return title

    def get_houses(self, html):
        selector = Selector(text=html)
        houses = selector.css('.listing')
        all_houses = []
        for house in houses:
            title = house.css('.title a::text').get()
            address = house.css('.address::text').getall()[-1].strip()
            price = house.css('.price::text').get()
            description = house.css('.description::text').get().strip()
            parser_db({'title': title, 'address': address, 'price': price, 'description': description})
            all_houses.append({
                'title': title,
                'address': address,
                'price': price,
                'description': description
            })
        return all_houses

if __name__ == '__main__':
    scraper = HousekgScraper()
    html = scraper.get_html()
    init_db()
    create_table()
    houses = scraper.get_houses(html)
    pprint(houses)