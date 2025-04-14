from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser
driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

# Do not enter anything - just submit
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait to see the error message
time.sleep(3)

# Optional: Print error message
error = driver.find_element(By.ID, "error-msg").text
print("Error message:", error)

# Close the browser
driver.quit()
