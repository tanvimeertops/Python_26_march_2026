from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.get("https://the-internet.herokuapp.com/")
# driver.get("https://the-internet.herokuapp.com/dynamic_content")
driver.get("https://the-internet.herokuapp.com/tables")


time.sleep(2)
# checkbox1=driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]")
# checkbox2=driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[2]")
# if not checkbox1.is_selected():
#     checkbox1.click()
# if (checkbox2.is_selected()):
#     checkbox2.click()
# # driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").click()
# time.sleep(10)

# driver.find_element(By.PARTIAL_LINK_TEXT,"Form").click()
# time.sleep(2)
# title="The Internet" 
# current_title=driver.title

# if(current_title==title):
#     print("Test case pass")
# print(current_title)
# time.sleep(10)

# Locate the visible “click here” link using XPath contains()
#  on its href or text. Refresh the 
# page and verify that the link can
# still be located.

# link=driver.find_element(By.XPATH,"//a[contains(text(),'click here')]")
# print("before refresh:",link.is_displayed())
# time.sleep(5)
# driver.refresh()
# refresh_link=driver.find_element(By.XPATH,"//a[contains(text(),'click here')]")
# print("after refresh:",refresh_link.is_displayed())
# time.sleep(5)

for i in range(1,4):
    for j in range(1,5):
        data=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr[" + str(i) + "]/td[" + str(j) + " ]").text
        print(data,end=' ')
        time.sleep(5)

        if(data=="Smith"):
            email=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr[" + str(i) + "]/td[3]").text
            print("smith's email:", email)