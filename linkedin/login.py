import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(5)


class LogIn:
    def __init__(self):

        self.username = 
        self.password = 

        self.username_input = driver.find_element(
            By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/div[1]/input"
        )
        self.password_input = driver.find_element(
            By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/div[2]/input"
        )
        self.login_button = driver.find_element(
            By.CLASS_NAME, "sign-in-form__submit-button"
        )

    def enter_credentiols(self):
        self.username_input.send_keys(self.username)
        self.password_input.send_keys(self.password)
        self.login_button.click()
        print("....loged in....")
