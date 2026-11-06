import string
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/web-table-element.php")
time.sleep(5)
row=driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr')
print(len(row))
col=driver.find_elements(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[1]/td')
print(len(col))

for i in range(1,len(row)+1):
    for j in range(1,len(col)+1):
        data=driver.find_element(By.XPATH,f'//*[@id="leftcontainer"]/table/tbody/tr[{i}]/td[{j}]').text
        print(data,end=' ')
    print()
    time.sleep(1)