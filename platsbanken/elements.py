from selenium.webdriver.common.by import By

from platsbanken.Page import driver

# lists
key_words = ["truckkort", "växjö", "it", "noggrann", "hittardudenhärärduintedålig"]

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

        # self.location = driver.find_element(
        #     By.XPATH,
        #     "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/section/pb-section-job-arbetsplats-position/div/div/div/div/strong[1]",
        # ).text

    def BaseCriterias(self, dataframe):
        if self.extent == "heltid" and self.duration == "tillsvidare":
            print(f"extent: {self.extent} \nduration: {self.duration}")
            for word in key_words:
                if word in self.adtext:
                    self.words_found = word

        else:
            if self.extent != "heltid":
                discard.append(dataframe)
            else:
                self.duration != "tillsvidare"
                discard.append(dataframe)

    def Suitebilety(self, dataframe):
        if len(self.words_found) >= 4:
            interesting.append(dataframe)
            # print(
            #     f"this is a interesting job!!! with these keywords in the ad -{interesting} that are located in {self.location}."
            # )

        elif len(self.words_found) >= 2:
            maybe.append(dataframe)
            # print(
            #     f"this is maybe a interesting job!!! with these keywords in the ad -{maybe} that are located in {self.location}."
            # )

        else:
            discard.append(dataframe)
        # print(f"this job sucks!!!{discard}")
