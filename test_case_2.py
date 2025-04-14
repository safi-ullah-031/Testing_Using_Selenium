from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")


driver.find_element(By.ID, "name").send_keys("Safi Ullah")
driver.find_element(By.ID, "email").send_keys("safi@invalid")  # Invalid email
driver.find_element(By.ID, "subject").send_keys("Invalid Email Test")
driver.find_element(By.ID, "message").send_keys("This is a test message. Sent using the Selenium WebDriver.")


driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


time.sleep(3)


error = driver.find_element(By.ID, "error-msg").text
print("Error message:", error)


driver.quit()
