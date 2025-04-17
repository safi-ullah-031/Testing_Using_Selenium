from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome driver
driver = webdriver.Chrome()

# Open website
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

# Wait explicitly for a specific condition
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "email")))

print("Element text:", element.text)

driver.quit()
