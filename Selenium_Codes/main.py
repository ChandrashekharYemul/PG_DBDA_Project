import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

driver = webdriver.Firefox()
driver.get("https://timesofindia.indiatimes.com/sports/hockey/top-stories/hockey-india-announces-40-probables-for-national-camp-to-prepare-for-home-series-against-germany/articleshow/113853173.cms")
# time.sleep(1)
title = []
h1 = driver.find_element(By.CLASS_NAME,'HNMDR')
title.append(h1.text)
article = []
div = driver.find_element(By.CLASS_NAME,'WEwSo')

article.append(div.text.replace(",",""))
# print(div.text)
# long = []
long_article = driver.find_element(By.CLASS_NAME,"okf2Z")
d1 = long_article.find_elements(By.TAG_NAME,'div')
cnt1 = 1
for i in d1:
    # print(i.text)
    # print("-"*80)
    # print(cnt)
    if cnt1 == 120:
        article.append(i.text.replace(",","").replace('\n',''))
        break
    cnt1+=1
all = []
all.append({
"Artical Id" : cnt,
"Artical Title": title,
"Artical Data": article

})
# all.append(article)
# all.append(long)

# print(title)
# print(short)
# print(long)
# print(d1.)
with open("SportsData.json",'w') as file:
    file.write(json.dumps(all))
with open("SportsData.csv",'a') as file:
    file.write('Artical Id,Artical Title,Artical Data\n')
    for item in all:
        file.write(f'{item['Artical Id']},{item['Artical Title']},{item['Artical Data']}\n')
driver.close()
