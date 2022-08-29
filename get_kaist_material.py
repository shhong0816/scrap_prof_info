import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

browser = webdriver.Chrome()

tot_num = 0
name = []
url = []
research_1 = []
research_2 = []
research_3 = []
research_4 = []




# browser.get("https://starlibrary.org/research/researcherByDept?searchInsttType=&searchName=732&page=1&insttType=")
# get_name = browser.find_element_by_xpath("//*[@id='researchersList']/div[2]/ul/li[2]/a[1]/strong")
# get_name.click()
# try:
#     url = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[1]/span/a")
# except:
#     url.append(X)



##각 페이지별 코딩하기
for pag_num in range(1,5):
    browser.get("https://starlibrary.org/research/researcherByDept?searchInsttType=kaist&searchName=9947&page={}&insttType=".format(pag_num))
    num = 1
    ##이름 get
    for count in range(len(browser.find_elements_by_class_name('year'))):
        get_name = browser.find_element_by_xpath("//*[@id='researchersList']/div[2]/ul/li[{}]/a[1]/strong".format(count+1))
        name.append(get_name.text)
        tot_num += 1
    ##각 사이트 들어가기-url얻#
    for count in range(len(browser.find_elements_by_class_name('year'))):
        get_name = browser.find_element_by_xpath("//*[@id='researchersList']/div[2]/ul/li[{}]/a[1]/strong".format(count+1))
        get_name.click()
        try:
            browser.switch_to_alert().accept()##alert 떠서 제2
            num += 1
            print(get_name.text,"불")
            url.append("None")
            research_1.append("None")
            research_2.append("None")
            research_3.append("None")
            research_4.append("None")
            continue
        except:
            no = 1
        browser.switch_to.window(browser.window_handles[1])##새로생긴 탭으로 이동
        try:
            url_get = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[1]/span/a")
            url.append(url_get.text)
        except:
            url.append("X")
        ####연구분야 얻-----1,2,3
        try:
            res_1 = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[3]/span/a[1]")
            research_1.append(res_1.text)
        except:
            research_1.append("X")
        try:
            res_2 = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[3]/span/a[2]")
            research_2.append(res_2.text)
        except:
            research_2.append("X")
        try:
            res_3 = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[3]/span/a[3]")
            research_3.append(res_3.text)
        except:
            research_3.append("X")
        try:
            res_4 = browser.find_element_by_xpath("//*[@id='researchersDetail']/div[1]/ul/li[3]/span/a[4]")
            research_4.append(res_4.text)
        except:
            research_4.append("X")
        ##다시 나가기
        browser.close()
        browser.switch_to.window(browser.window_handles[0])##기존 탭으로이동
        time.sleep(0.5)
        print(get_name.text,"완",num,"/",len(browser.find_elements_by_class_name('year')),"pag number =",pag_num)##오래걸리니까 얼마나했는지 체
        num += 1








with open("kaist_material.csv","w", encoding = 'cp949',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(name)
    write.writerow(url)
    write.writerow(research_1)
    write.writerow(research_2)
    write.writerow(research_3)
    write.writerow(research_4)

print("Fin",tot_num,"명 존재g")
