from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")


driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


time.sleep(3)


error = driver.find_element(By.ID, "error-msg").text
print("Error message:", error)


driver.quit()
