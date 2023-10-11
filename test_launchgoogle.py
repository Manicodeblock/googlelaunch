import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

class smpl():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)

    def test_lgn(self):
        print("Login world wide test started")
        time.sleep(3)
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.login("standard_user", "secret_sauce")

    def login(self, username, password):
        print("Login world wide test started")
        time.sleep(1)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        time.sleep(2)
        # password : secret_sauce     user name is standard_user
        username_var = self.driver.find_element(By.XPATH, "//input[@type='text']")
        password_var = self.driver.find_element(By.XPATH, "//input[@type='password']")
        submit_var = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username_var.clear()
        time.sleep(1)
        username_var.send_keys(username)
        time.sleep(1)
        password_var_status = password_var.is_displayed()
        if password_var_status == True:
            password_var.clear()
            time.sleep(1)
            password_var.send_keys(password)
            time.sleep(2)
            submit_var.click()
            time.sleep(5)
            submit_var_status = submit_var.is_displayed()
            if submit_var_status == True:
                print("Loggin failed")
            else:
                print("Loggin success")
        else:
            nextbutton_var = self.driver.find_element(By.XPATH,
                                                      "//*[(text()='Next') or (text()='next') or (text()='continue') or (text()='Continue')]")
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


# searchbar_xpath = "//*[@type='text']"
# searchicon_xpath = "//*[@xmlns='http://www.w3.org/2000/svg']"
# searchitem_xpath = "//*[text()='APPLE iPhone 14 ((PRODUCT)RED, 128 GB)']"
# button_buynow_xpath = "//*[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']"
# closemark_xpath = "//*[@class='_2KpZ6l _2doB4z']"
# print("***** Functionality started *****")
# driver.get("https://www.flipkart.com/")
# # time.sleep(2)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, closemark_xpath).click()
# time.sleep(2)
#
# driver.find_element(By.XPATH, searchbar_xpath).click()
# time.sleep(2)
# driver.find_element(By.XPATH, searchbar_xpath).send_keys("iphone14")
# time.sleep(2)
# driver.find_element(By.XPATH, searchicon_xpath).click()
# time.sleep(2)
# driver.find_element(By.XPATH,searchitem_xpath).click()
# time.sleep(8)
# source = driver.find_element(By.XPATH,button_buynow_xpath)
# time.sleep(2)
# action.move_to_element(source).click().perform()
# # action.move_to_element(source).click().perform()
# time.sleep(2)
# current_url = driver.current_url
# print("***** Functionality End *****")







