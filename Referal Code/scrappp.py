# from requests_html import HTMLSession
# session = HTMLSession()
# url="https://www.moneycontrol.com/news/tags/nifty.html/page-2/"
# r=session.get(url)
# r.html.render(sleep=1,scrolldown=5)
# articles=r.html.find('h2')
# print(articles)
from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.moneycontrol.com/news/tags/nifty.html/page-2/"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify())
title =soup.title
paras=soup.find_all(['a'])
# print(paras)
# print(soup.find('h2')['class']) 
# print(soup.find_all('h2',class_="market_newstitle"))
# print(soup.find('h2').get_text()) 
# for text in paras:
#     print(text.get('title'))

s=soup.find
q=soup.find(id="category")
for i in paras:
    print(i.get('title'))