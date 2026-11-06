from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/popup.php")


main_w=driver.current_window_handle
print(main_w)

driver.find_element(By.PARTIAL_LINK_TEXT,"Cli").click()
time.sleep(2)
all_w=driver.window_handles
print(all_w)
time.sleep(2)


for child_w in all_w:
    if child_w!=main_w:
            driver.switch_to.window(child_w)
            time.sleep(2)
            print("child window:"+child_w)
            driver.find_element(By.NAME,"emailid").send_keys("123")
            time.sleep(5)
            driver.close()
            time.sleep(5)

driver.switch_to.window(main_w)
current_w=driver.current_window_handle
print("current window : "+current_w)
time.sleep(2)
driver.close()


