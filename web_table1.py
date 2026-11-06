import string

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("file:///D:\Python\Python_26_march\index1.html")
time.sleep(5)


for i in range(2,5):
    for j in range(1,5):
        data1=driver.find_element(By.XPATH,
        f"/html/body/table/tbody/tr[{i}]/td[{j}]").text
        print(data1)