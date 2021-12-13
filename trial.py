from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mpi4py import MPI

PATH = "/Users/pranavvinod/Documents/GitHub/HPSC-Project/chromedriver"
# driver = webdriver.Chrome(PATH)
# start = time.time()
# driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
# titles = driver.find_elements_by_id("video-title")
# for title in titles:
#     print(title.text)
#     print("")

# driver.quit()


# # PATH = "https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL"
# driver = webdriver.Chrome(PATH)
# driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL")
# titles2 = driver.find_elements_by_id("video-title")
# for title in titles2:
#     print(title.text)
#     print("")


# driver.quit()
# end = time.time()
# print('Time taken is: ',end-start)

################################################################################################################
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

start = time.time()
if rank==0:
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC")
    titles = driver.find_elements_by_id("video-title")
    for title in titles:
        print(title.text)
        print("")

    driver.quit()

if rank==1:
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.youtube.com/playlist?list=PLirAqAtl_h2o4xCWaBsDH3BKNQs8YqLCL")
    titles2 = driver.find_elements_by_id("video-title")
    for title in titles2:
        print(title.text)
        print("")
    driver.quit()

end = time.time()
print("The time taken is: ",end-start)

MPI.Finalize()