from bs4 import BeautifulSoup
import requests
prices = []
page_link ='https://www.abw.by/car/sell/ford/c-max/?search=1&type=1&sort=&capacity1=&capacity2=&mileage1=&mileage2=&year1=2003&year2=&price1=&price2=7000&country=1&text=&day='
# fetch the content from url

with requests.get(page_link, timeout=5) as page_response:
    page_content = BeautifulSoup(page_response.content, "html.parser")

# years = page_content.find(class_='data-second-item data-year 1')
def desc_avto():
    avto_box = page_content.find('div', class_='product-full clearfix js-product ')
    title_box = avto_box.find('div', class_='title')
    title = title_box.text.strip()
    print('title:', title)
    description_box = avto_box.find('div', class_='description')
    description = description_box.text.strip()
    print('description:', description)
    # print('title:', title)
    years_box = avto_box.find('div', class_='data-second-item data-year 1')
    year = years_box.span.string
    print('year:', year)
    mileage_box = avto_box.find(class_='mileage')
    mileage = mileage_box.text.strip()
    print('mileage:', mileage)
    location_box = avto_box.find(class_='location')
    location = location_box.text.strip()
    print('location:', location)
    prices_box = avto_box.find(class_='data-price-usd')
    price = prices_box.text.strip()
    print('price:', price)
    link_box = avto_box.a['href']
    print(link_box)
    print('\n')

desc_avto()

# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'data-price-usd'})
