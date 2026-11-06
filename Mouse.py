import string
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(5)
home=driver.find_element(By.LINK_TEXT,'Home')
flight=driver.find_element(By.LINK_TEXT,'Flights')
hotel=driver.find_element(By.LINK_TEXT,'Hotels')
actions=ActionChains(driver)
actions.move_to_element(home).perform()
time.sleep(2)
actions.move_to_element(flight).perform()
time.sleep(2)
actions.move_to_element(hotel).perform()
time.sleep(5)