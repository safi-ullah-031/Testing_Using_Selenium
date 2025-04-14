from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser
driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

# Fill the form with valid data
driver.find_element(By.ID, "name").send_keys("Safi Ullah")
driver.find_element(By.ID, "email").send_keys("safi@example.com")
driver.find_element(By.ID, "subject").send_keys("Automation Testing")
driver.find_element(By.ID, "message").send_keys("This is a test message. Test using the Selenium WebDriver.")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait to see result
time.sleep(3)

# Close the browser
driver.quit()
