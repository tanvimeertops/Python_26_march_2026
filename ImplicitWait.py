from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")




driver.find_element(By.XPATH,"//input[@name='email']").send_keys("1234")    

email=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("value")
print(email)
# driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("1234")
time.sleep(5)















