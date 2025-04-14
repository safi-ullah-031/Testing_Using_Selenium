from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start the Chrome WebDriver
driver = webdriver.Chrome()

# Open a sample form (you can replace this with your own)
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

# Optional: Maximize window
driver.maximize_window()

# Wait until the input fields are present
try:
    # Wait for the first input (First name)
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="name"]'))
    )
    first_name_input.clear()
    first_name_input.send_keys("John")

    # Wait for the second input (email)
    last_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="email"]'))
    )
    last_name_input.clear()
    last_name_input.send_keys("Doe@gmail.com")

    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="subject"]'))
    )
    subject_input.clear()
    subject_input.send_keys("This is a test")

    Message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="message"]'))
    )
    Message_input.send_keys("This is a test message send by the selenium to test the webdriver and selenium installation")


    # Find and click the submit button (here it's a regular button)
    submit_btn = driver.find_element(By.XPATH, '//button[text()="Send Message"]')
    submit_btn.click()

    # Wait and view the result (if any)
    time.sleep(3)

except Exception as e:
    print("Error:", e)

# Close the browser
driver.quit()
