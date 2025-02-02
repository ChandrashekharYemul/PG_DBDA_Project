import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

driver = webdriver.Firefox()
driver.get("https://timesofindia.indiatimes.com/sports/badminton")

idx = 1
cnt = 0
for i in range(1, 43):
    print(i)
    # mintv = driver.find_element(By.CLASS_NAME,"close_btn_minitv")
    # mintv.click()
    time.sleep(2)

    f1 = driver.find_elements(By.CLASS_NAME, 'small')
    f2 = []
    for j in f1:
        f2 += j.find_elements(By.CLASS_NAME, 'cvs_wdt')

    list1 = []
    for k in f2:
        list1 += k.find_elements(By.CLASS_NAME, 'w_tle')
    list1[cnt].click()
    # if cnt != 24:
    #     list1[cnt].click()
    # else:
    #     cnt += 1
    #     continue



    title = []
    h1 = driver.find_element(By.CLASS_NAME, 'HNMDR')
    title.append(h1.text)

    article = []
    div = driver.find_element(By.CLASS_NAME, 'WEwSo')
    article.append(div.text.replace(",", "").replace("\\","").replace("\n",""))

    long_article = driver.find_element(By.CLASS_NAME, "okf2Z")
    d1 = long_article.find_elements(By.TAG_NAME, 'div')
    cnt1 = 1
    for i in d1:
        if cnt1 == 120:
            article.append(i.text.replace(",", "").replace('\n', '').replace("\\",""))
            break
        cnt1 += 1

    all = []
    all.append({
        "Artical Id": idx,
        "Artical Title": title,
        "Artical Data": article

    })
    idx += 1


    # with open("SportsData.json", 'w') as file:
    #     file.write(json.dumps(all))
    with open("SportsDataBadminton.csv", 'a') as file:
        file.write('Artical Id,Artical Title,Artical Data\n')
        for item in all:
            file.write(f'{item['Artical Id']},{item['Artical Title']},{item['Artical Data']}\n')

    driver.back()
    cnt += 1

driver.close()