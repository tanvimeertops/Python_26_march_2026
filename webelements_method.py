from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.get("https://www.instagram.com/?hl=en")
#driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.get("https://practice.expandtesting.com/radio-buttons")

# title=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]")
# print(title.text)
# time.sleep(2)
#button[normalize-space()='Disable']
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(2)
# user_name=driver.find_element(By.ID,"user-name").get_attribute("value")
# print(user_name)
# time.sleep(2)
# driver.find_element(By.ID,"login-button").click()
# time.sleep(2)
# ele_error=driver.find_element(By.XPATH,"//div[@class='error-message-container error']")
# print(ele_error.is_displayed())
# if ele_error:
#     print(ele_error.text)
time.sleep(5)
# button=driver.find_element(By.XPATH,"//button[normalize-space()='Enable']")
# print(button.is_enabled())
# button.click
# print(button.is_enabled())

checkbox=driver.find_element(By.XPATH,"(//div[@class='row']//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]")
# print(checkbox.is_selected())
checkbox.click()
# print(checkbox.is_selected())

