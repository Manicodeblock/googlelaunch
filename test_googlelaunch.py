import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get("https://www.google.com/")
time.sleep(4)
print("Google launched successfully")
currenturl = driver.current_url
print("current url")
print(currenturl)
time.sleep(3)
driver.close()

