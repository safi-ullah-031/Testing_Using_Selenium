from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser
driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

# Fill the form with invalid email
driver.find_element(By.ID, "name").send_keys("Safi Khan")
driver.find_element(By.ID, "email").send_keys("safi@invalid")  # Invalid email
driver.find_element(By.ID, "subject").send_keys("Invalid Email Test")
driver.find_element(By.ID, "message").send_keys("This is a test.")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait to see the error message
time.sleep(3)

# Optional: Print error message (if any)
error = driver.find_element(By.ID, "error-msg").text
print("Error message:", error)

# Close the browser
driver.quit()
