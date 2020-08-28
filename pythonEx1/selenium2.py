'''
Created on 2020. 8. 25.

@author: GDJ24
네이버 로그인
'''
from selenium import webdriver # pip install selenium
import time
# chromedriver.eve 파일 다운로드 :
# https://chromedriver.chromium.org/downloads
# 크롬의 버전에 맞는 파일 다운받기. 크롬 도움말 > 크롬 정보
# D: > setup/chromedriver -> 위치에 chromedriver.eve 파일 복사
driver = webdriver.Chrome("D:/setup/chromedriver")
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

id = input("네이버 아이디를 입력하세요.")
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'") # javascript 실행
pw = input("네이버 비밀번호를 입력하세요.")
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
driver.find_element_by_xpath('//*[@id="log.login"]').click() # id가 log.login인 것을 찾아서 클릭해라.
# xpath을 이용하여 지정한 태그 객체 한개에 접근

