from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  

driver = webdriver.Chrome()
driver.get("http://sqap-demo.com.pafiastcommunity.com/")

print(driver.title) 

driver.quit()
