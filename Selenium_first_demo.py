'''
webdriver is a tool for automating web application testing,
 and in this code, we are using it to open a web browser and perform some actions on a webpage. The code below demonstrates how to set up a Selenium WebDriver instance and navigate to a specific URL.
'''
import time

from selenium import webdriver
#empty browser window
driver =webdriver.Edge()
#opening a webpage
driver.get("https://www.google.com")
time.sleep(5)
print(driver.current_url)
print(driver.title)
# driver.quit #close entire browser
driver.close() #close the tab
time.sleep(5)
