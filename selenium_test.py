from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Chrome browser
driver = webdriver.Chrome()  # or provide path: webdriver.Chrome(executable_path="path_to_chromedriver")

# Open your form page
driver.get("http://sqap-demo.com.pafiastcommunity.com/")  # Replace with your form URL

# Fill out the form fields
driver.find_element(By.NAME, "username").send_keys("test_user")
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("securepassword123")

# Submit the form
driver.find_element(By.ID, "submit-btn").click()  # Use the correct selector for your button

# Wait and close
time.sleep(3)
driver.quit()
