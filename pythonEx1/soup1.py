'''
Created on 2020. 8. 24.

@author: GDJ24
크롤링 예제 // 자바의 Jsonp과 비슷하다.
'''
from bs4 import BeautifulSoup # pip install beautifulsoup4
html = '''
    <html><body>
        <div id="potal">
            <h1>포털 목록</h1>
            <ul class="items">
                <li><a href="http://www.naver.com">naver</a></li>
                <li><a href="http://www.daum.net">daum</a></li>
            </ul>
        </div>
    </body></html>
'''
# soup : html 문자열을 dom의 형태로 파싱하여 최상위 객체로 리턴
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
links = soup.find_all("a") # a 태그 전체
for a in links :
    href = a.attrs["href"]
    text = a.string # a 태그의 값
    print(text,">",href)
# select_one : 선택된 태그 1개
# id 속성의 값이 potal인 div 태그의 하위태그인 h1 태그를 선택
h1 = soup.select_one("div#potal> h1").string
print("h1=",h1)

li_list = soup.select("div#potal > ul.items > li")
for li in li_list :
    print("li=",li.string)