from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
# driver.get("https://demo.guru9ll9.com/test/radio.html")

# time.sleep(2)
# radio=driver.find_element(By.ID,"vfb-7-1")
# print(radio.is_selected())
# time.sleep(2)
# radio.click()
# time.sleep(2)
# print(radio.is_selected())


driver.get("https://demo.guru99.com/test/newtours/register.php")
time.sleep(5)
webele=Select
t(driver.find_element(By.NAME,"country"))
webele.select_by_index(1)
time.sleep(2)
webele.select_by_value("INDIA")
time.sleep(2)
webele.select_by_visible_text("VATICAN CITY")
time.sleep(5)