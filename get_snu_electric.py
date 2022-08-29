import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

browser = webdriver.Chrome()
browser.get("http://ee.snu.ac.kr/faculty/professor")
time.sleep(1)
element = browser.find_element_by_tag_name('body')
element.send_keys(Keys.END)

num = 0
name = []
url = []
research_1 = []
research_2 = []
research_3 =[]
research_4 = []


##이름 갯수 확인
# browse_data = browser.find_elements_by_class_name("name")
# print(len(browse_data))


##이름 가져오
for k in range(62):
    browse_data = browser.find_elements_by_class_name("name")
    get_name = browse_data[k].find_element_by_tag_name("a")
    name.append(get_name.text)
print("get name완료")

##url get
for k in range(62):
    browse_data = browser.find_elements_by_css_selector("[title*='새창으로 열림']")
    get_url = browse_data[k].text
    url.append(get_url)
print(url)
print("url 완료")


##research get
for k in range(62):
    browse_data = browser.find_elements_by_class_name("research")
    get_re = browse_data[k].text
    research_1.append(get_re)
print("get url완료")


with open("seoul_electric.csv","w", encoding = 'cp949',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(name)
    write.writerow(url)
    write.writerow(research_1)


print("Fin")
