from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element_by_name("q") #특정 검색어 찾기
elem.send_keys("손흥민") #원한는 값 입력
elem.send_keys(Keys.RETURN) #엔터키 전송
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click() #클래스명 사용여러개 이미지 불러와 담기 #python selenium click, 첫번째 요소
#큰 이미지 선택해 다운

#assert "Python" in driver.title
#elem = driver.find_element_by_name("q") 
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()