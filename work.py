import requests
from bs4 import BeautifulSoup as bs

class Username:
    def __init__(self, url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
       }
        self.soup=None
    def auditSite(self):
        response=requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text, "html.parser")
        else:
            print("Не вдалось підключитися до сайту")
    def getInfo(self):
        usernames=[]
        listNames=self.soup.find('tbody')
        if not listNames:
            print('помилка в пошуку')
            return usernames
        info=listNames.find_all('tr')[0:10]
        for i in info:
            name=i.find('div',class_='table-cell-value tm-value')
            name2=name.text.strip() if name else "відсутній юз"
            price=i.find("div",class_="table-cell-value tm-value icon-before icon-ton")
            price2=price.text.strip()+str(" toncoins") if price else "відсутня ціна"
            usernames.append({
                'назва':name2,
                'ціна':price2,
            })
        return usernames
    def showInfo(self,usernames):
        print('N\t', 'Назва', '\t', '    ціна')
        print('-'*50)
        num=1
        for i in usernames:
            print(num,'\t',i['назва'],'\t',i["ціна"])
            num+=1

url="https://fragment.com/?sort=listed&filter=sale"
obj=Username(url)
obj.auditSite()
obj.getInfo()
site=obj.getInfo()
print('\n10 юзернеймів які нещодавно виставили на продаж\n')
if site:
    obj.showInfo(site)
else:
    print("жодної інформаціі не отримано")


if site:
    print("\nппокупка")
    num = input("який юз хочете купити? введіть тількі номер з ліва: ")
    num = int(num)
    kolvo = input("кількість: ")
    kolvo = int(kolvo)
    price = site[num-1]['ціна']
    price = price[0:price.find(" ")]
    price = float(price)
    total = price * kolvo
    print("\nВаш заказ:")
    print(str(int(total)) + " toncoins")