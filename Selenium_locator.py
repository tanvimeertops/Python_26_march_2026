from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
#driver.get("https://demoqa.com/buttons")
driver.get("https://www.facebook.com/")
# driver.get("https://www.geeksforgeeks.org/")
time.sleep(5)
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(2)
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.ID,"login-button").click()
# time.sleep(5)

# driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# time.sleep(2)
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(2)
# driver.find_element(By.NAME,"login-button").click()
# time.sleep(5)

#driver.find_element(By.TAG_NAME,"button").click()

#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"D").click()

# driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("1234")
# driver.find_element(By.CSS_SELECTOR,".input_error form_input").send_keys("1234")
# driver.find_element(By.CSS_SELECTOR,"[placeholder='Username']").send_keys("standard_user")
# driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("1234")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"[placeholder='Password']").send_keys("secret_sauce")
# time.sleep(5)
# driver.quit()

# #static xpath
# driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys("standard_user")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='password']").send_keys("secret_sauce")
# time.sleep(5)

#dynamic xpath
# //<tag name>[@attribute='value']
# //<tag_name>[text()='value']
# //input[@name='email']

driver.find_element(By.XPATH,"//input[@name='email']").send_keys("1234")    
time.sleep(5)
email=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("value")
print(email)
# driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("1234")
time.sleep(5)


