from numpy import source
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
html = driver.find_element_by_tag_name("html")
for i in range(95):
    time.sleep(1)
    html.send_keys(Keys.PAGE_DOWN)

links = [x.get_attribute('href') for x in driver.find_elements(By.ID,"video-title")]
print(len(links))

#Creating local lists 
split = len(links)/4
min = int(rank*split)
maxi = int((rank+1)*split)
l_links = links[min:maxi]


if rank==0:
    start = time.time()
   
    for link in l_links[0:5]:
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
    end = time.time()
    t0 = end -start
    t1 = comm.recv(source=1,tag=1)
    t2 = comm.recv(source=2,tag=1)
    t3 = comm.recv(source=2,tag=1)

    df0 = comm.recv(source=1,tag=2)
    df = df.append(df0)

    dfa = comm.recv(source=2,tag=2)
    df=df.append(dfa)

    dfb = comm.recv(source=3,tag=2)
    df=df.append(dfb)

    
    t = max(t0,t1,t2,t3)
    df = df.append(df0)
    print("The total runtime is: ",t)
    df.to_csv("1playlist_4cores")
    driver.quit()
    
########################################################################################

if rank==1:
    start = time.time()
   
    for link in l_links[0:5]:
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
            df1.loc[len(df1.index)]=x
        except:
            continue

    end = time.time()
    t1 = end-start
    comm.send(t1,dest=0,tag=1)
    comm.send(df1,dest=0,tag=2)
    
    driver.quit()

#################################################################################

if rank==2:
    start = time.time()
   
    for link in l_links[0:5]:
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
            df2.loc[len(df2.index)]=x
        except:
            continue

    end = time.time()
    t1 = end-start
    comm.send(t1,dest=0,tag=1)
    comm.send(df2,dest=0,tag=2)
    
    driver.quit()

    #####################################################################################

if rank==3:
    start = time.time()
   
    for link in l_links[0:5]:
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
            df3.loc[len(df3.index)]=x
        except:
            continue

    end = time.time()
    t1 = end-start
    comm.send(t1,dest=0,tag=1)
    comm.send(df3,dest=0,tag=2)
    
    driver.quit()

MPI.Finalize()