from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

website_url = "http://sqap-demo.com.pafiastcommunity.com/"
driver.get(website_url)


time.sleep(2)


screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

print(f"Screenshot saved at {screenshot_path}")


driver.quit()
