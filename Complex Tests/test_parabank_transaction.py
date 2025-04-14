from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/")
driver.maximize_window()

# Login
driver.find_element(By.NAME, "username").send_keys("john")
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.CSS_SELECTOR, "input.button").click()
time.sleep(3)

# Click Transfer Funds
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
time.sleep(2)

# Enter transaction details
driver.find_element(By.ID, "amount").send_keys("500")
time.sleep(1)

# Submit transaction
driver.find_element(By.CSS_SELECTOR, "input.button").click()
time.sleep(3)

# Verify transaction message
message = driver.find_element(By.CSS_SELECTOR, "h1.title").text
print("Transaction Result:", message)

time.sleep(5)
driver.quit()
