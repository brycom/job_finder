import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from login import LogIn, driver


def job_button():
    button = driver.find_element(
        By.XPATH, "/html/body/div[6]/header/div/nav/ul/li[3]/a"
    )
    button.click()


class SearchInput:
    def __init__(self):
        self.basic_search = driver.find_element(
            By.XPATH,
            "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]",
        )
        self.location_input = driver.find_element(
            By.XPATH,
            "/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[1]",
        )

    def insert_value(self):
        self.basic_search.send_keys("fortnox")
        self.location_input.send_keys("växjö")
        time.sleep(2)
        self.location_input.send_keys(Keys.RETURN)


class GetCardContainers:
    def __init__(self):
        self.container_list = driver.find_elements(
            By.CLASS_NAME, "scaffold-layout__list-container"
        )

    def containers(self):
        for i in self.container_list:
            ad_link = i.get_attribute("id")
            print(f"link for the ad: {ad_link}")


test = LogIn()

test.enter_credentiols()


job_button()
search_linkedin = SearchInput()
search_linkedin.insert_value()
time.sleep(4)
test1 = GetCardContainers()
test1.containers()
time.sleep(4)
driver.quit()
