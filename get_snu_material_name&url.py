import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time


num = 0
name = []
data = []

browser = webdriver.Chrome()

#총8페이지 8페이지는 노가다 왜냐면 4개
for i in range(7):
    browser.get("https://eng.snu.ac.kr/professor?department%5B0%5D=45&title=&page="+str(i))
    time.sleep(1)
    element = browser.find_element_by_tag_name('body')

    ##이름 가져오
    for k in range(1,6):
        get_name = browser.find_element_by_xpath("//*[@id='block-system-main']/div/div/div[2]/ul/li["+str(k)+"]/dl/dt/a")
        name.append(get_name.text)
    # print("get name완료")

    ##그 외 정보 다 가져오기
    for k in range(1,6):
        get_data = browser.find_element_by_xpath("//*[@id='block-system-main']/div/div/div[2]/ul/li["+str(k)+"]/dl/dd")
        data.append(get_data.text)
    print(chr(i)+'page 완료')

with open("get_names_info.csv","w", encoding = 'cp949',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(name)
    write.writerow(data)

print("Fin")
