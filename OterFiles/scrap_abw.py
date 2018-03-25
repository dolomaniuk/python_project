from bs4 import BeautifulSoup
import requests
import csv
avtomobil = []
page_link ='https://www.abw.by/car/sell/ford/c-max/?search=1&type=1&sort=&capacity1=&capacity2=&mileage1=&mileage2=&year1=2003&year2=&price1=&price2=7000&country=1&text=&day=30&photo=1'


def desc_avto(new_avto_block):
    title_box = new_avto_block.find('div', class_='title')
    title = title_box.text.strip()
    print('title:', title)
    description_box = new_avto_block.find('div', class_='description')
    description = description_box.text.strip()
    print('description:', description)
    years_box = new_avto_block.find('div', class_='data-second-item data-year 1')
    year = years_box.span.string
    print('year:', year)
    mileage_box = new_avto_block.find(class_='mileage')
    mileage = mileage_box.text.strip()
    print('mileage:', mileage)
    location_box = new_avto_block.find(class_='location')
    location = location_box.text.strip()
    print('location:', location)
    prices_box = new_avto_block.find(class_='data-price-usd')
    price = prices_box.text.strip()
    print('price:', price)
    link = new_avto_block.a['href']
    print(link)
    # print('\n')

    with open('abw.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, description, year, mileage, location, price, link])

with requests.get(page_link, timeout=5) as page_response:
    page_content = BeautifulSoup(page_response.content, "html.parser")

# find all blocks with avto's ad
avto_box = page_content.find_all('div', class_='product-full clearfix js-product ')

# for each ad use parsing
for _ in avto_box:
    desc_avto(_)

print('\nНайдено всего {} объявлений, поданных за последний месяц'.format(len(avto_box)))
# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'data-price-usd'})

# open a csv file with append, so old data will not be erased