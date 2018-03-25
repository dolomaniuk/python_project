from bs4 import BeautifulSoup
import requests
import csv
import configparser

# TODO - если объявок больше чем 1 страница


avtomobil = []
page_link = 'https://www.abw.by/car/sell/'

config = configparser.ConfigParser()
config.read('avto_to_search.ini')

avto_brand = config.get('AVTO', 'brand')
avto_model = config.get('AVTO', 'model')
avto_year_from = config.get('AVTO', 'year_from')
avto_year_to = config.get('AVTO', 'year_to')
avto_price_from = config.get('AVTO', 'price_from')
avto_price_to = config.get('AVTO', 'price_to')
avto_country = config.get('AVTO', 'country')
avto_days = config.get('AVTO', 'days')
avto_photo = config.get('AVTO', 'photo')

# config.add_section('AVTO')
# config.set('AVTO', 'avto_brand', 'ford')
# config.set('AVTO', 'avto_model', 'c-max')
# config.set('AVTO', 'avto_year_from', '2001')
# config.set('AVTO', 'avto_year_to', '')
# config.set('AVTO', 'avto_price_from', '')
# config.set('AVTO', 'avto_price_to', '7000')
# config.set('AVTO', 'avto_country', '1')
# config.set('AVTO', 'avto_days', '30')
# config.set('AVTO', 'avto_photo', '1')

# # save to a file
# with open('avto.ini', 'w') as configfile:
#     config.write(configfile)

page_link += avto_brand + '/'
page_link += avto_model + '/'
page_link += '?search=1&type=1&sort=&capacity1=&capacity2=&mileage1=&mileage2=&year1='
page_link += avto_year_from + '&'
page_link += 'year2=' + avto_year_to + '&'
page_link += 'price1=' + avto_price_from + '&'
page_link += 'price2=' + avto_price_to + '&'
page_link += 'country=' + avto_country + '&'    # Беларусь
page_link += 'text=&day=' + avto_days + '&' # за какой период показывать объявки
page_link += 'photo=' + avto_photo  # показывать только с фото

print(page_link)

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