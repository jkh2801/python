'''
Created on 2020. 8. 25.

@author: GDJ24
selenium 예제
'''
from selenium import webdriver # pip install selenium
import time
# chromedriver.eve 파일 다운로드 :
# https://chromedriver.chromium.org/downloads
# 크롬의 버전에 맞는 파일 다운받기. 크롬 도움말 > 크롬 정보
# D: > setup/chromedriver -> 위치에 chromedriver.eve 파일 복사
driver = webdriver.Chrome("D:/setup/chromedriver")
driver.get("http://python.org")

menus = driver.find_elements_by_css_selector("#top ul.menu li")
print(type(menus))
pypi = None
for m in menus:
    if m.text == "PyPI" :
        pypi = m
    print(m.tag_name, m.text)

pypi.click() # 출력
time.sleep(5) # 5초 대기
driver.quit() # 브라우저 종료