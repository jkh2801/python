'''
Created on 2020. 8. 24.

@author: GDJ24
크롤링 예제
'''
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
title = soup.find("title").string
''' 
<![CDATA[ .... ]]> => CDATA 섹션 표시 => 순수한 문자열 영역
PDATA : parsing 되는 데이터 영역
'''
wf = soup.find("wf").string
print(title)
print(wf)
for w in wf.split("<br />") :
    print(w)