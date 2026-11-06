from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")

time.sleep(2)
driver.find_element(By.XPATH
                    ,"//input[@name='cusid']").send_keys("12345")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='submit']").click()


a1=driver.switch_to.alert
print(a1.text)
time.sleep(2)
# a1.dismiss()
a1.accept()
time.sleep(5)
a2=driver.switch_to.alert
print(a2.text)
time.sleep(2)
a2.accept()
time.sleep(5)
driver.close()