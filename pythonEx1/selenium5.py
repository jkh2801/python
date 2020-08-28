'''
Created on 2020. 8. 25.

@author: GDJ24
'''
import time
from selenium import webdriver

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
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click() # id가 log.login인 것을 찾아서 클릭해라.
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/a').click() # id가 log.login인 것을 찾아서 클릭해라.
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/div/div[3]/ul[2]/li[2]/a').click() # id가 log.login인 것을 찾아서 클릭해라.
time.sleep(1) # 브라우저를 띄우기 위해 약간의 시간을 부여한다.
products = driver.find_elements_by_css_selector(".goods_pay_section")
for product in products:
    print("-", product.text)
time.sleep(2)
driver.quit()
