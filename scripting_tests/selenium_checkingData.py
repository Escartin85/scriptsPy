from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\batman\Downloads\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.phptravels.net/offers');

b_tags = driver.find_elements_by_tag_name('b')

price_list = []

for b in b_tags:
    price_list.append(b.text)

print(price_list)

clean_list = []

for price in price_list:
    if price.startswith('USD'):
        price_number = price[5:]
        integer_price = int(price_number.replace(',',''))
        clean_list.append(integer_price)

print(sorted(clean_list))
