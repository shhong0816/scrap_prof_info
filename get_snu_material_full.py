import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

browser = webdriver.Chrome()
browser.get("https://mse.snu.ac.kr/sub.php?code=faculty&mode=&category=51&orderType=user_name&orderBy=asc")
time.sleep(1)
element = browser.find_element_by_tag_name('body')
element.send_keys(Keys.END)

num = 0
data = []
url = []
email = []
research_1 = []
research_2 = []
research_3 =[]
research_4 = []


##이름 가져오####xpath가 사실 더 쉬울듯
browse_data_L = browser.find_elements_by_class_name("profBoxL")
for data_L in browse_data_L:
    data_L_name = data_L.find_element_by_class_name("txt1")
    data.append(data_L_name.text)
    num += 1

browse_data_R = browser.find_elements_by_class_name("profBoxR")
for data_R in browse_data_R:
     data_R_name = data_R.find_element_by_class_name("txt1")
     data.append(data_R_name.text)
     num += 1

print("get name완료")

##클릭으로 들어가 url get

for count in range(16):
    data_L = browser.find_elements_by_class_name("profBoxL")
    data_L_go_url = data_L[count].find_element_by_class_name("detail")
    data_L_go_url.find_element_by_tag_name("a").click()
    ##browser.switch_to.window(browser.window_handles[0])##기존 탭으로이동으로 browser 초기화가능
    time.sleep(0.1)
    get_url = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[1]/li[8]/p/a")
    url.append(get_url.text)
    time.sleep(0.1)
    browser.back()
    time.sleep(0.1)

for count in range(15):
    data_R = browser.find_elements_by_class_name("profBoxR")
    data_R_go_url = data_R[count].find_element_by_class_name("detail")
    data_R_click = data_R_go_url.find_element_by_tag_name("a").click()
    time.sleep(0.1)
    get_url = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[1]/li[8]/p/a")
    url.append(get_url.text)
    time.sleep(0.1)
    browser.back()
    time.sleep(0.1)
print("get url 완pr")

##클릭으로 들어가 email,research get
for count in range(16):
    data_L = browser.find_elements_by_class_name("profBoxL")
    data_L_go_url = data_L[count].find_element_by_class_name("detail")
    data_L_go_url.find_element_by_tag_name("a").click()
    time.sleep(0.1)
    get_email = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[1]/li[4]/p")
    email.append(get_email.text)
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[1]")
        research_1.append(get_re.text)
    except:
        research_1.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[3]")
        research_2.append(get_re.text)
    except:
        research_2.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[5]")
        research_3.append(get_re.text)
    except:
        research_3.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[7]")
        research_4.append(get_re.text)
    except:
        research_4.append("X")
    time.sleep(0.1)
    browser.back()
    time.sleep(0.1)

for count in range(15):
    data_R = browser.find_elements_by_class_name("profBoxR")
    data_R_go_url = data_R[count].find_element_by_class_name("detail")
    data_R_click = data_R_go_url.find_element_by_tag_name("a").click()
    time.sleep(0.1)
    get_email = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[1]/li[4]/p")
    email.append(get_email.text)
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[1]")
        research_1.append(get_re.text)
    except:
        research_1.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[3]")
        research_2.append(get_re.text)
    except:
        research_2.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[5]")
        research_3.append(get_re.text)
    except:
        research_3.append("X")
    try:
        get_re = browser.find_element_by_xpath("/html/body/div[5]/div/div/ul[2]/li[3]/ul[2]/li[7]")
        research_4.append(get_re.text)
    except:
        research_4.append("X")
    time.sleep(0.1)
    browser.back()
    time.sleep(0.1)





with open("seoul_material.csv","w", encoding = 'cp949',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(data)
    write.writerow(url)
    write.writerow(email)
    write.writerow(research_1)
    write.writerow(research_2)
    write.writerow(research_3)
    write.writerow(research_4)

print("Fin")
