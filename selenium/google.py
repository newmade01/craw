from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #시간을 지연시켜주는 코드
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element_by_name("q") #특정 검색어 찾기
elem.send_keys("손흥민") #원한는 값 입력
elem.send_keys(Keys.RETURN) #엔터키 전송

#scroll Down
SCROLL_PAUSE_TIME = 1 #대기시간이 너무 적으면 중도에 정지됌  버튼 나오기전

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True: #무한반복
    # Scroll down to bottom, 브라우저 끝까지 스크롤 내림
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page=0.5초동안
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height, 브라우저의 높이를 구해 새로운 높이 구함
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() #스크롤이 맨 아래로 내려갈 때 더보기 클릭
        except: #실패시
            break
    last_height = new_height
    #스크롤이 끝까지 내려간 것으로 인식해 break걸림


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #클래스명 사용여러개 이미지 불러와 담기 #python selenium click, 첫번째 요소
count = 1
for image in images:
    image.click() #이미지 클릭
    time.sleep(3)   #시간지연
    imageUrl=driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #큰 이미지 선택해 다운

    urllib.request.urlretrieve(imageUrl, str(count)+"손흥민.jpg") #주소, 저장하고자 하는 이미지 이름

    count=count+1 #반복할때마다 숫자 파일 변경

driver.close() #웹브라우저 닫기