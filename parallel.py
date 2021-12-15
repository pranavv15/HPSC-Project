from typing import SupportsRound
from numpy import source
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
df1 = pd.DataFrame(columns=c)
df2 = pd.DataFrame(columns=c)
df3 = pd.DataFrame(columns=c)


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
    d1 = comm.recv(source=1,tag=7)
    df1 = df1.append(d1)
    d2 = comm.recv(source=2,tag=8)
    df1 = df1.append(d2)
    d3 = comm.recv(source=3,tag=9)
    df1 = df1.append(d3)
    n= num+n2+n3+n4
    df1.to_csv("most_views_parallel")

    print("The total titles are: ",n)
    print("The time taken is: ",t)

######################################################################################


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
            df1.loc[len(df1.index)]=x
        except:
            continue
   
    print(df1.head())
    driver.quit()
    end = time.time()
    t2 = end-start
    comm.send(t2,dest = 0,tag = 1)
    comm.send(num,dest=0,tag=4)
    comm.send(df1,dest=0,tag=7)
 

 #######################################################################################




if rank==2:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2p57Njt3QJDtwxAPZENJrIp")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)

    links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
    print(len(links))

    for link in links:
        try:
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
            df2.loc[len(df2.index)]=x
        except:
            continue
    print(df2.head())
    driver.quit()
    end = time.time()
    t3 = end-start
    comm.send(t3,dest = 0,tag = 2)
    comm.send(num,dest=0,tag=5)
    comm.send(df2,dest=0,tag=8)

########################################################################################



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
            print(x)
            df3.loc[len(df3.index)]=x
        except:
            continue

    print(df3.head())
    driver.quit()
    end = time.time()
    t4 = end-start
    comm.send(t4,dest = 0,tag = 3)
    comm.send(num,dest=0,tag=6)
    comm.send(df3,dest=0,tag=9)

MPI.Finalize()