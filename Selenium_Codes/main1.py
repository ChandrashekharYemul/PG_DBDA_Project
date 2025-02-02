import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

driver = webdriver.Firefox()
driver.get("https://timesofindia.indiatimes.com/sports/hockey")
for i in range(1,38):
    print(i)
    f1 = driver.find_elements(By.CLASS_NAME,'small')
    # print(len(f1))
    mainclass = []
    for i in f1:
        mainclass += i.find_elements(By.CLASS_NAME, 'cvs_wdt')
    # print(len(mainclass))
    list1 = []
    for i in mainclass:
        list1 += i.find_elements(By.CLASS_NAME,'w_tle')

    print(len(list1))
    print(list1)

    for i in list1:
        i.click()
        driver.back()
# list1 = mainclass.find_elements(By.NAME,'Hockey News')


    # time.sleep(5)
# driver.close()
# j = []
# for i in list:
#     j = i.find_element(By.CLASS_NAME,'w_tle')
#     j.click()
# #     break
#     time.sleep(5)
#     driver.close()

# j[0].click()

driver.close()
# list[0].click()


# title = []
# h1 = driver.find_element(By.CLASS_NAME,'HNMDR')
# title.append(h1.text)
# article = []
# div = driver.find_element(By.CLASS_NAME,'WEwSo')
#
# article.append(div.text.replace(",",""))
# # print(div.text)
# # long = []
# long_article = driver.find_element(By.CLASS_NAME,"okf2Z")
# d1 = long_article.find_elements(By.TAG_NAME,'div')
# cnt = 1
# for i in d1:
#     # print(i.text)
#     # print("-"*80)
#     # print(cnt)
#     if cnt == 120:
#         article.append(i.text.replace(",","").replace('\n',''))
#         break
#     cnt+=1
# all = []
# all.append({
# "Artical Id" : 4,
# "Artical Title": title,
# "Artical Data": article
#
# })
# # all.append(article)
# # all.append(long)
#
# # print(title)
# # print(short)
# # print(long)
# # print(d1.)
# with open("SportsData.json",'w') as file:
#     file.write(json.dumps(all))
# with open("SportsData.csv",'a') as file:
#     file.write('Artical Id,Artical Title,Artical Data\n')
#     for item in all:
#         file.write(f'{item['Artical Id']},{item['Artical Title']},{item['Artical Data']}\n')

