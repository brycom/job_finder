import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from Page import driver, job_list, runging_page

# Driver.
# url = "https://arbetsformedlingen.se/platsbanken/annonser/26579203"
# driver = webdriver.Chrome("C:\python\chromedriver.exe")
# driver.get(url)
# driver.implicitly_wait(5)

# lists
key_words = ["truckkort", "växjö", "it", "noggrann", "hittardudenhärärduintedålig"]
words_found = []
discard = []
maybe = []
interesting = []


# Elements.
class CheckAds:
    def __init__(self):
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

        self.location = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/section/pb-section-job-arbetsplats-position/div/div/div/div/strong[1]",
        ).text

    def BaseCriterias(self):
        if self.extent == "heltid" and self.duration == "tillsvidare":
            print(f"extent: {self.extent} \nduration: {self.duration}")
            for word in key_words:
                if word in self.adtext:
                    words_found.append(word)

        else:
            driver.quit()

    def Suitebilety(self):
        if len(words_found) >= 4:
            interesting.append(words_found)
            print(
                f"this is a interesting job!!! with these keywords in the ad -{interesting} that are located in {self.location}."
            )

        elif len(words_found) >= 2:
            maybe.append(words_found)
            print(
                f"this is maybe a interesting job!!! with these keywords in the ad -{maybe} that are located in {self.location}."
            )

        else:
            discard.append(words_found)
            print(f"this job sucks!!!{discard}")


# Loop through al the ad's.


# Check if the jobb is fulltime and continues. Done


# Compear with keywords and evalueat the compatebilety of the job. Done


# Pandas datafram with [index , Company and City: , Job description: , Ad link: ]
runging_page()
df = pd.DataFrame(job_list)
df_colum = df["Ad link:"]

for i in df_colum:
    driver.get(i)
    time.sleep(2)
    run_ad = CheckAds()
    run_ad.BaseCriterias()
    run_ad.Suitebilety()


# read_csv("C:\python\Projects\selenium\job finder\platsbanken\jobs_platsbanken.csv",delimiter=",",ad_links = df["Ad link:"]print(df.iloc[0:4])

# for ad in ad_links:
#    url.append(ad)


# base_criterias()
# suitebilety()


driver.quit()
# Get all elemets.
# Convert al text to lowercase. done
# Base criterias: done
# Check if the job is fulltime. done
# Check if duration is tillsvidare. done
# If the two abuve is true.done
# Get description text.done


# Search for keywords.done

# Sourt by amount of keywords found by if elif else.done

# Return full description from pandas dataframe in the categoris pased on keyword hits.
