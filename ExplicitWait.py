from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,90)

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click me to start timer']").click()
time.sleep(15)
txt=wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='WebDriver']"))).text
print(txt)