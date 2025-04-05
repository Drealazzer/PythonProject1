# #шаблон
# # from http.client import responses
# #
# # import requests
# # from bs4 import BeautifulSoup as bs
# #
# # class Name:
# #     def __init__(self, url):
# #         self.url=url
# #         self.header={
# #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# #        }
# #         self.soup=None
# #     def auditSite(self):
# #         response=requests.get(self.url,headers=self.header)
# #         if response.status_code==200:
# #             self.soup=bs(response.text, "html.parser")
# #         else:
# #             print("Не вдалось підключитися до сайту")
# #     def getInfo(self):
# #         pass
# #     def showInfo(self):
# #         pass
# # url="посилання"
# # obj=Name(url)
# # obj.auditSite()
# # obj.getInfo()
# # site=obj.getInfo()
# # if site:
# #     obj.showInfo()
# # else:
# #     print("жодної інформаціі не отримано")
from traceback import print_tb

# import requests
# from bs4 import BeautifulSoup as bs
#
# class comfy:
#     def __init__(self, url):
#         self.url=url
#         self.header={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#        }
#         self.soup=None
#     def auditSite(self):
#         response=requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text, "html.parser")
#         else:
#             print("Не вдалось підключитися до сайту")
#             return
#     def getInfo(self):
#         laptop=[]
#         lap=self.soup.find_all('div',class_="products-catalog")
#         if not lap:
#             print("помилка в пошуку на сторінці")
#             return
#         for i in laptop[0:4]:
#             name=i.find('a',class_="prdl-item__name ellipsis-2-lines")
#             nameError=name.text.strip() if name else "відсутня назва"
#             # if name:
#             #     name.text()
#             # else:
#             #     print("відсутня назва")
#             price=i.find("div",class_="products-list-item-price__actions-price-current")
#             priceError=price.text.strip() if price else "відсутня ціна"
#             laptop.append(
#                 {
#                     'назва':nameError,
#                     'ціна':priceError,
#                 }
#             )
#         return laptop
#     def showInfo(self, laptop):
#         print('N\t','Назва','\t*2','ціна','\t*2')
#         print('-'*50)
#         for i in laptop:
#             print('\t',i['назва'],'\t',i['ціна'])
#
# url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# obj=comfy(url)
# obj.auditSite()
# obj.getInfo()
# site=obj.getInfo()
# print('\tнайпопулярніши 4 ноутбуки\n')
# if site:
#     obj.showInfo(site)
# else:
#     print("жодної інформаціі не отримано")


import requests
from bs4 import BeautifulSoup as bs

class Coin:
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
        coins=[]
        listCoin=self.soup.find('tbody')
        if not listCoin:
            print('помилка в пошуку')
            return coins
        info=listCoin.find_all('tr')[0:10]
        for i in info:
            name=i.find('p',class_='coin-item-name')
            name2=name.text.strip() if name else "відсутня назва"
            price=i.find("div",class_="sc-142c02c-0 lmjbLF")
            price2=price.text.strip() if price else "відсутня ціна"
            coins.append({
                'назва':name2,
                'ціна':price2,
            })
        return coins
    def showInfo(self,coins):
        print('N\t', 'Назва', '\t', '    ціна')
        print('-'*50)
        num=1
        for i in coins:
            print(num,'\t',i['назва'],'\t',i['ціна'])
            num+=1
url="https://coinmarketcap.com/"
obj=Coin(url)
obj.auditSite()
obj.getInfo()
site=obj.getInfo()
print('5 найпопулярніших кріпто монет')
if site:
    obj.showInfo(site)
else:
    print("жодної інформаціі не отримано")