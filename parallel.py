from typing import SupportsRound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mpi4py import MPI

PATH = "/Users/pranavvinod/Documents/GitHub/HPSC-Project/chromedriver"
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num=0
if rank==0:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
    titles = driver.find_elements_by_id("video-title")
    for title in titles:
        # print(title.text)
        # print("")
        num+=1
    
    driver.quit()
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
    titles2 = driver.find_elements_by_id("video-title")
    for title in titles2:
        # print(title.text)
        # print("")
        num+=1
    driver.quit()
    end = time.time()
    t2 = end-start
    comm.send(t2,dest = 0,tag = 1)
    comm.send(num,dest=0,tag=4)




if rank==2:
    start = time.time()
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2p57Njt3QJDtwxAPZENJrIp")
    html = driver.find_element_by_tag_name("html")
    for i in range(95):
        time.sleep(1)
        html.send_keys(Keys.PAGE_DOWN)
    titles3 = driver.find_elements_by_id("video-title")
    for title in titles3:
        # print(title.text)
        # print("")
        num+=1
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
    titles4 = driver.find_elements_by_id("video-title")
    for title in titles4:
        # print(title.text)
        # print("")
        num+=1
    driver.quit()
    end = time.time()
    t4 = end-start
    comm.send(t4,dest = 0,tag = 3)
    comm.send(num,dest=0,tag=6)


# print("The time taken is: ",end-start)

MPI.Finalize()