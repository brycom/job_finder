import time

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())  # type: ignore
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(5)


class LogIn:
    def __init__(self):

        self.username = "mathiasbrynolf20@gmail.com"
        self.password = "Dazun1997"

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
