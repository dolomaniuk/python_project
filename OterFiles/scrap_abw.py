from bs4 import BeautifulSoup
import requests
import csv
import os
avtomobil = []
page_link ='https://www.abw.by/car/sell/ford/c-max/?search=1&type=1&sort=&capacity1=&capacity2=&mileage1=&mileage2=&year1=2003&year2=&price1=&price2=7000&country=1&text=&day=30&photo=1'


def desc_avto(new_avto_block, x):
    title_box = new_avto_block.find('div', class_='title')
    avtomobil.append(title_box.text.strip())
    description_box = new_avto_block.find('div', class_='description')
    avtomobil.append(description_box.text.strip())
    years_box = new_avto_block.find('div', class_='data-second-item data-year 1')
    avtomobil.append(years_box.span.string)
    mileage_box = new_avto_block.find(class_='mileage')
    avtomobil.append(mileage_box.text.strip())
    location_box = new_avto_block.find(class_='location')
    avtomobil.append(location_box.text.strip())
    prices_box = new_avto_block.find(class_='data-price-usd')
    avtomobil.append(prices_box.text.strip())
    avtomobil.append(new_avto_block.a['href'])

    # write to csv file
    try:
        with open('abw.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [avtomobil[x], avtomobil[x + 1], avtomobil[x + 2], avtomobil[x + 3], avtomobil[x + 4], avtomobil[x + 5],
                 avtomobil[x + 6]])
    except:
        print("File abw.csv can't be created or opened")

with requests.get(page_link, timeout=5) as page_response:
    page_content = BeautifulSoup(page_response.content, "html.parser")

# find all blocks with avto's ad
avto_box = page_content.find_all('div', class_='product-full clearfix js-product ')


# cleaning abw.csv
try:
    with open('abw.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

    # for each ad use parsing
    i = 0  # counter for column
    for _ in avto_box:
        desc_avto(_, i)
        i += 7
    print('\nНайдено всего {} объявлений, поданных за последний месяц'.format(len(avto_box)))
except:
    print("File abw.csv can't be cleaned")


# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'data-price-usd'})

# open a csv file with append, so old data will not be erased