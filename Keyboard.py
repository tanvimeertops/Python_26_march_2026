import string
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

email=driver.find_element(By.NAME,"email")
actions=ActionChains(driver)
actions.move_to_element(email).click().key_down(Keys.SHIFT).send_keys("tanvi").key_up(Keys.SHIFT).double_click().context_click().perform()
time.sleep(2)


