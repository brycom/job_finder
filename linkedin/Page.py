import time

from login import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url_list = []


def job_button():
    button = driver.find_element(By.XPATH, "/html/body/nav/ul/li[4]/a")
    button.click()


class SearchInput:
    def __init__(self):
        self.basic_search = driver.find_element(
            By.NAME,
            "keywords",
        )

        self.location_input = driver.find_element(
            By.NAME,
            "location",
        )

    def insert_value(self, key_words: str, location: str):
        self.basic_search.send_keys(key_words)
        self.location_input.clear()
        self.location_input.send_keys(location)
        time.sleep(1)
        self.location_input.send_keys(Keys.RETURN)


class GetCardContainers:
    def __init__(self):
        self.container_list = driver.find_elements(By.PARTIAL_LINK_TEXT, "/jobs/view/")

    def containers(self):
        for i in self.container_list:
            print(f"link for the ad: {i}")


def get_url():

    container = driver.find_elements(
        By.TAG_NAME,
        "li",
    )
    for c in container:
        hyperlink = c.find_element(
            By.XPATH, "/html/body/div[3]/div/main/section[2]/ul/li[1]/a"
        )
        url = hyperlink.get_attribute("href")
        url_list.append(url)


driver.maximize_window()
job_button()
time.sleep(2)
search_linkedin = SearchInput()
search_linkedin.insert_value("testare", "växjö")
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
finally:
    pass
get_url()


driver.quit()
