import requests
from bs4 import BeautifulSoup as BS
import lxml

url = 'https://www.currency.me.uk/convert/usd/uah'
r = requests.get(url)
#для збору даних з сайту
soup = BS(r.text, 'lxml')
course = soup.find("span", {"class": "mini ccyrate"}).text
#виведення курсу доллара до гривні
print(course)