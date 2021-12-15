from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random

c=['Title','Likes','Views','Uploaded Date']
df = pd.DataFrame(columns=c)
rate = [i/10 for i in range(10)]
num=0
PATH = "/Users/pranavvinod/Documents/GitHub/HPSC-Project/chromedriver"
driver = webdriver.Chrome(PATH)
start = time.time()
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")

html = driver.find_element(By.TAG_NAME,"html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)

links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
print(len(links))

for link in links:
    try:
        print(num)
        num+=1
        driver.get(link)
        time.sleep(4)

        names = driver.find_elements(By.ID, "info")
        x = (names[2].text.split("\n"))
        if(len(x)>6):
            if(x[0][0]=='#'):
                x.pop(0)
        x.remove("DISLIKE")
        x.remove("SHARE")
        x.remove("SAVE")
        s = x[1].split(' views')
        for i in s:
            x.append(i) 
        x.pop(1)
        # print(x)
        df.loc[len(df.index)]=x
    except:
        continue
# # print(df)
# # time.sleep(random.choice(rate))

# print(len(links))
# end = time.time()
# print("The time taken is: ",end-start)
print(df.head())
driver.quit()

#######################################################################################

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)
links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]

 
for link in links:
    try:
        driver.get(link)
        time.sleep(4)

        names = driver.find_elements(By.ID, "info")
        x = (names[2].text.split("\n"))
        if(len(x)>6):
            if(x[0][0]=='#'):
                x.pop(0)
        x.remove("DISLIKE")
        x.remove("SHARE")
        x.remove("SAVE")
        s = x[1].split(' views')
        for i in s:
            x.append(i) 
        x.pop(1)
        # print(x)
        df.loc[len(df.index)]=x
    except:
        continue

print(len(links))
driver.quit()

# ######################################################################################

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2p57Njt3QJDtwxAPZENJrIp")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)
links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
for link in links:
    try:
        driver.get(link)
        time.sleep(4)

        names = driver.find_elements(By.ID, "info")
        x = (names[2].text.split("\n"))
        if(len(x)>6):
            if(x[0][0]=='#'):
                x.pop(0)
        x.remove("DISLIKE")
        x.remove("SHARE")
        x.remove("SAVE")
        s = x[1].split(' views')
        for i in s:
            x.append(i) 
        x.pop(1)
        df.loc[len(df.index)]=x
    except:
        continue

print(len(links))
driver.quit()

# ###########################################################################################

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2rTbOXU2Oc-7WBBHmFrnyUC")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(5)
    html.send_keys(Keys.PAGE_DOWN)
links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
for link in links:
    try:
        driver.get(link)
        time.sleep(4)

        names = driver.find_elements(By.ID, "info")
        x = (names[2].text.split("\n"))
        if(len(x)>6):
            if(x[0][0]=='#'):
                x.pop(0)
        x.remove("DISLIKE")
        x.remove("SHARE")
        x.remove("SAVE")
        s = x[1].split(' views')
        for i in s:
            x.append(i) 
        x.pop(1)
        df.loc[len(df.index)]=x
    except:
        continue


print(len(links))
driver.quit()
end = time.time()
print('Time taken is: ',end-start)
df.to_csv("most_views_serial.csv")

################################################################################################################


