from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.implicitly_wait(10)


driver.get("http://sqap-demo.com.pafiastcommunity.com/")


element = driver.find_element(By.ID, "email")

print("Element text:", element.text)

driver.quit()
