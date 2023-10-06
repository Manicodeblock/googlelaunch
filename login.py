import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

class comfunction:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):

        username_var = self.driver.find_element(By.XPATH,"//input[@type='text']")
        password_var = self.driver.find_element(By.XPATH, "//input[@type='password']")
        submit_var = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username_var.clear()
        time.sleep(1)
        username_var.send_keys(username)
        time.sleep(1)
        password_var_status = password_var.is_displayed()
        if password_var_status == True :
            password_var.clear()
            time.sleep(1)
            password_var.send_keys(password)
            time.sleep(2)
            submit_var.click()
            time.sleep(5)
            submit_var_status=submit_var.is_displayed()
            if submit_var_status == True:
                print("Loggin failed")
            else:
                print("Loggin success")
        else:
            nextbutton_var = self.driver.find_element(By.XPATH,"//*[(text()='Next') or (text()='next') or (text()='continue') or (text()='Continue')]")
            time.sleep(2)
            nextbutton_var.click()
            time.sleep(2)
            password_var.clear()
            time.sleep(2)
            password_var.send_keys(password)
            time.sleep(2)
            submit_var.click()
            time.sleep(5)
            submit_var_status = submit_var.is_displayed()
            if submit_var_status == True:
                print("Loggin failed")
            else:
                print("Loggin success")










