from login import driver
from selenium.webdriver.common.by import By

search_words = ["testare", "test", "it"]
discard = []
maybe = []
interesting = []


def show_more_button():
    driver.find_element(
        By.XPATH,
        '//*[@id="main-content"]/section[1]/div/div/section/div/div/section/button[1]',
    ).click()


class CheckAds:
    def __init__(self):

        self.words_found = []

        self.extent = driver.find_element(
            By.XPATH,
            "/html/body/main/section[1]/div/div/section/div/ul/li[2]/span",
        ).text.lower()

        self.adtext = driver.find_element(
            By.XPATH,
            "/html/body/main/section[1]/div/div/section/div/div/section/div",
        ).text.lower()

    def BaseCriterias(self, dataframe):
        if self.extent == "heltid":
            print(f"extent: {self.extent}")
            for word in search_words:
                if word in self.adtext:
                    self.words_found = word

        else:
            if self.extent != "heltid":
                discard.append(dataframe)
                print(f"extent: {self.extent}")

    def Suitebilety(self, dataframe):
        if len(self.words_found) >= 4:
            interesting.append(dataframe)

        elif len(self.words_found) >= 2:
            maybe.append(dataframe)

        else:
            discard.append(dataframe)
