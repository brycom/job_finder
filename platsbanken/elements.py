from selenium.webdriver.common.by import By

from platsbanken.Page import driver

# lists

discard = []
maybe = []
interesting = []


# Elements.
class CheckAds:
    def __init__(self):

        self.words_found = []

        self.extent = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/div[2]/div[1]/span[2]",
        ).text.lower()

        self.duration = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/section/pb-section-job-quick-info/div[2]/div[2]/span[2]",
        ).text.lower()

        self.adtext = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/section/pb-section-job-main-content/div",
        ).text.lower()

    def BaseCriterias(self, dataframe):
        if self.extent == "heltid" and self.duration == "tillsvidare":
            print(f"extent: {self.extent} \nduration: {self.duration}")
            for word in search_words:
                if word in self.adtext:
                    self.words_found = word

        else:
            if self.extent != "heltid":
                discard.append(dataframe)
                print(f"extent: {self.extent} \nduration: {self.duration}")
            else:
                self.duration != "tillsvidare"
                discard.append(dataframe)
                print(f"extent: {self.extent} \nduration: {self.duration}")

    def Suitebilety(self, dataframe):
        if len(self.words_found) >= 4:
            interesting.append(dataframe)

        elif len(self.words_found) >= 2:
            maybe.append(dataframe)

        else:
            discard.append(dataframe)
