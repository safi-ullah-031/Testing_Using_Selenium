from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")


driver.find_element(By.ID, "name").send_keys("Safi Ullah")
driver.find_element(By.ID, "email").send_keys("safi@example.com")
driver.find_element(By.ID, "subject").send_keys("Automation Testing")
driver.find_element(By.ID, "message").send_keys("This is a test message. Sent using the Selenium WebDriver.")


driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


time.sleep(3)


driver.quit()
