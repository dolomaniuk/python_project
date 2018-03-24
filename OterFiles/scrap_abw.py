from bs4 import BeautifulSoup
import requests
prices = []
page_link ='https://www.abw.by/car/sell/ford/c-max/?search=1&type=1&sort=&capacity1=&capacity2=&mileage1=&mileage2=&year1=2003&year2=&price1=&price2=7000&country=1&text=&day='
# fetch the content from url

with requests.get(page_link, timeout=5) as page_response:
    page_content = BeautifulSoup(page_response.content, "html.parser")

# years = page_content.find(class_='data-second-item data-year 1')

mileage_box = page_content.find(class_='mileage')
mileage = mileage_box.text.strip()
print('mileage:', mileage)
years_box = page_content.find(class_='data-second-item data-year 1')
year = years_box.span.text.strip()
print('year:', year)
prices_box = page_content.find(class_='data-price-usd')
price = prices_box.text.strip()
print('price:', price)


# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# you can also access the main_price class by specifying the tag of the class
# prices = page_content.find_all('div', attrs={'class':'data-price-usd'})
