from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(2)
driver.switch_to.frame(0)
time.sleep(2)
txt=driver.find_element(By.XPATH,"//h1[normalize-space()='The iframe element']").text
print(txt)