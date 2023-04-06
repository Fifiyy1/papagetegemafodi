from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.oschadbank.ua/")
#перевірка підключення
if response.status_code == 200:
#об'єкт парсінгу - назва сторінки та обробника
   soup = BeautifulSoup(response.text, features="html.parser")
   soup_list = soup.find_all("span", {"class": "currency__item_value"})
   for elem in soup_list:
       print(soup_list[0].text)

