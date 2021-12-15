from typing import SupportsRound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mpi4py import MPI
import pandas as pd

PATH = "/Users/pranavvinod/Documents/GitHub/HPSC-Project/chromedriver"
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num=0
c=['Title','Likes','Views','Uploaded Date']
df = pd.DataFrame(columns=c)

# driver = webdriver.Chrome(PATH)
# driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
# html = driver.find_element_by_tag_name("html")
# for i in range(95):
#     time.sleep(1)
#     html.send_keys(Keys.PAGE_DOWN)

# links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
# print(len(links))
# k = len(links)/4

# local_links = links[k*rank:(k+1)*rank]



if rank==0:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
    
    links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
    print(len(links))
    for link in links:
        try:
            # print(num)
            num+=1
            driver.get(link)
            time.sleep(4)

            names = driver.find_elements(By.ID, "info")
            # for name in names:
                # print(name.text.split("\n"))

            x = (names[2].text.split("\n"))
            if(len(x)>6):
                if(x[0][0]=='#'):
                    x.pop(0)
            x.remove("DISLIKE")
            x.remove("SHARE")
            x.remove("SAVE")
            # x.append(x[1].split("views")[i] for i in range(2))
            s = x[1].split(' views')
            for i in s:
                x.append(i) 
            x.pop(1)
            # print(x)
            df.loc[len(df.index)]=x
        except:
            continue

    print(df.head())
    end = time.time()
    t1 = end - start
    t2 = comm.recv(source = 1, tag=1)
    t3 = comm.recv(source=2,tag=2)
    t4 = comm.recv(source=3,tag=3)
    t= max(t1,t2,t3,t4)
    n2 = comm.recv(source = 1, tag=4)
    n3 = comm.recv(source=2,tag=5)
    n4 = comm.recv(source=3,tag=6)
    n= num+n2+n3+n4
    print("The total titles are: ",n)
    print("The time taken is: ",t)


if rank==1:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
    links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
    print(len(links))

    for link in links:
        try:
        # print(num)
            num+=1
            driver.get(link)
            time.sleep(4)

            names = driver.find_elements(By.ID, "info")
            # for name in names:
                # print(name.text.split("\n"))

            x = (names[2].text.split("\n"))
            if(len(x)>6):
                if(x[0][0]=='#'):
                    x.pop(0)
            x.remove("DISLIKE")
            x.remove("SHARE")
            x.remove("SAVE")
            # x.append(x[1].split("views")[i] for i in range(2))
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
    end = time.time()
    t2 = end-start
    comm.send(t2,dest = 0,tag = 1)
    comm.send(num,dest=0,tag=4)
    # end = time.time()
    # t2 = end-start




if rank==2:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2p57Njt3QJDtwxAPZENJrIp")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
    # 
    links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
    print(len(links))

    for link in links:
        try:

            # print(num)
            num+=1
            driver.get(link)
            time.sleep(4)

            names = driver.find_elements(By.ID, "info")
            # for name in names:
                # print(name.text.split("\n"))

            x = (names[2].text.split("\n"))
            if(len(x)>6):
                if(x[0][0]=='#'):
                    x.pop(0)
            x.remove("DISLIKE")
            x.remove("SHARE")
            x.remove("SAVE")
            # x.append(x[1].split("views")[i] for i in range(2))
            s = x[1].split(' views')
            for i in s:
                x.append(i) 
            x.pop(1)
            # print(x)
            df.loc[len(df.index)]=x
        except:
            continue
    print(df.head())
    driver.quit()
    end = time.time()
    t3 = end-start
    comm.send(t3,dest = 0,tag = 2)
    comm.send(num,dest=0,tag=5)




if rank==3:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2rTbOXU2Oc-7WBBHmFrnyUC")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
   
    links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
    print(len(links))

    for link in links:
        try:
            # print(num)
            num+=1
            driver.get(link)
            time.sleep(4)

            names = driver.find_elements(By.ID, "info")
            # for name in names:
                # print(name.text.split("\n"))

            x = (names[2].text.split("\n"))
            if(len(x)>6):
                if(x[0][0]=='#'):
                    x.pop(0)
            x.remove("DISLIKE")
            x.remove("SHARE")
            x.remove("SAVE")
            # x.append(x[1].split("views")[i] for i in range(2))
            s = x[1].split(' views')
            for i in s:
                x.append(i) 
            x.pop(1)
            print(x)
            df.loc[len(df.index)]=x
        except:
            continue

    print(df.head())
    driver.quit()
    end = time.time()
    t4 = end-start
    comm.send(t4,dest = 0,tag = 3)
    comm.send(num,dest=0,tag=6)


# print("The time taken is: ",end-start)

MPI.Finalize()