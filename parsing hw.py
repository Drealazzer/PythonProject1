import requests
from bs4 import BeautifulSoup as bs
class Book:
    def __init__(self,url):
        self.url =url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response= requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text, "html.parser")
        else:
            print("не вдалось підключитися до сайту")
    def getInfo(self):
        books = []
        listBooks=self.soup.find_all('article',class_='product_pod')[0:8]
        if not listBooks:
            print("помилка в пошуку")
            return books
        for i in listBooks:
            name=i.find('h3').find('a')
            name2=name['title'].strip() if name else "відсутня назва"
            price=i.find('p', class_='price_color')
            price2=price.text.strip() if price else "відсутня ціна"
            rating=i.find('p', class_='star-rating')
            rating2=rating['class'][1] if rating and len(rating['class'])>1 else "відсутній рейтинг"
            books.append({
                'назва':name2,
                'ціна':price2,
                'рейтинг':rating2+' stars',
            })
        return books
    def showInfo(self, books):
        print('N''\t''Назва''\t''\t''Ціна''\t''\t''Рейтинг')
        print('-' *50)
        num=1
        for i in books:
            print(num, '\t', i['назва'], '\t', i['ціна'], '\t', i['рейтинг'])
            num += 1
url="http://books.toscrape.com"
obj=Book(url)
obj.auditSite()
obj.getInfo()
site = obj.getInfo()
print('8 книг із сайту')
if site:
    obj.showInfo(site)
else:
    print("жодної інформаціі не отримано")
