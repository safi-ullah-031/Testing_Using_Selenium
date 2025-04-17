from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# Open the website
website_url = "http://sqap-demo.com.pafiastcommunity.com/"
driver.get(website_url)

# Wait for the page to fully load
time.sleep(2)

# Take a screenshot and save it
screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

print(f"Screenshot saved at {screenshot_path}")

# Close the browser
driver.quit()
