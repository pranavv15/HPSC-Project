from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy
import pandas as pd

num=0
li=["Video Titles"]

PATH = "/Users/pranavvinod/Documents/GitHub/HPSC-Project/chromedriver"
driver = webdriver.Chrome(PATH)
start = time.time()
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")

html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)

titles = driver.find_elements_by_id("video-title")
for title in titles:
    # print(title.text)
    li.append(title.text)
    num=num+1
    # print("")
print(num)
driver.quit()

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)
titles2 = driver.find_elements_by_id("video-title")
for title in titles2:
    num+=1
    li.append(title.text)
print(num)
driver.quit()

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2p57Njt3QJDtwxAPZENJrIp")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)
titles3 = driver.find_elements_by_id("video-title")
for title in titles3:

    li.append(title.text)

    num+=1
print(num)
driver.quit()

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2rTbOXU2Oc-7WBBHmFrnyUC")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)
titles4 = driver.find_elements_by_id("video-title")
for title in titles4:
 
    li.append(title.text)

    num+=1
df = pd.DataFrame(li)
print(len(df))
df.to_csv("youtube_data.csv",index=False)
driver.quit()
end = time.time()
print('Time taken is: ',end-start)

################################################################################################################


