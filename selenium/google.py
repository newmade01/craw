from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #시간을 지연시켜주는 코드
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element_by_name("q") #특정 검색어 찾기
elem.send_keys("손흥민") #원한는 값 입력
elem.send_keys(Keys.RETURN) #엔터키 전송
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #클래스명 사용여러개 이미지 불러와 담기 #python selenium click, 첫번째 요소
count = 1
for image in images:
    image.click() #이미지 클릭
    time.sleep(3)   #시간지연
    imageUrl=driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #큰 이미지 선택해 다운

    urllib.request.urlretrieve(imageUrl, str(count)+"손흥민.jpg") #주소, 저장하고자 하는 이미지 이름

    count=count+1 #반복할때마다 숫자 파일 변경


#assert "Python" in driver.title
#elem = driver.find_element_by_name("q") 
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()