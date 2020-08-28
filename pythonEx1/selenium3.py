'''
Created on 2020. 8. 25.

@author: GDJ24
url에서 제공되는 html의 내용을 BeautifulSoup 모듈로 파싱
pandas 모듈을 이용하여 csv 파일로 생성
'''
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup # pip install BeautifulSoup

driver = webdriver.Chrome("D:/setup/chromedriver")
driver.get("https://oscar.go.com/winners")
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')
oscars_2020 = []
for item in zip(category, movie, producer):
    oscars_2020.append({
        'category' : item[0].text,
        'movie' : item[1].text,
        'producer' : item[2].text
        })
data = pd.DataFrame(oscars_2020)
print(data)
data.to_csv('oscars_2020.csv')
driver.quit()