# This test is for the form which contain existant valid data.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.get("http://sqap-demo.com.pafiastcommunity.com/")


driver.maximize_window()


try:
    
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="name"]'))
    )
    first_name_input.clear()
    first_name_input.send_keys("Test")
    time.sleep(2)
    # Wait for the second input (email)
    last_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="email"]'))
    )
    last_name_input.clear()
    last_name_input.send_keys("test@gmail.com")
    time.sleep(2)
    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="subject"]'))
    )
    subject_input.clear()
    subject_input.send_keys("This is a test")
    time.sleep(2)
    Message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@id="message"]'))
    )
    Message_input.clear()
    Message_input.send_keys("This is a test message send by the selenium to test the webdriver and selenium installation")
    
    time.sleep(3)

    
    submit_btn = driver.find_element(By.XPATH, '//button[text()="Send Message"]')
    submit_btn.click()

    
    time.sleep(3)

except Exception as e:
    print("Error:", e)


driver.quit()
