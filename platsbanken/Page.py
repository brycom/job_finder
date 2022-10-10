from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:mmot_H3A_auW"
driver = webdriver.Chrome("C:\python\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(5)

# list for pd dataframe.
job_list = []


# Decline cookis.
def click_decline_button():
    decline_button = driver.find_element(By.ID, "afCookieDecline")
    decline_button.click()


# locate and sort children
def item_organizer(containers):
    for i in containers:
        job_ad = i.find_element(By.TAG_NAME, "a")
        ad_link = job_ad.get_attribute("href")
        job_description = job_ad.text
        company_and_city = i.find_element(By.CLASS_NAME, "pb-company-name").text

        job_items = {
            "Company and City:": company_and_city,
            "Job description:": job_description,
            "Ad link:": ad_link,
        }

        job_list.append(job_items)


# Locate and puch the next button.
def next_page():

    next_button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button/span[1]/span",
    )
    next_button.click()


# run!!
def runging_page():
    click_decline_button()

    while driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button/span[1]/span",
    ):
        main_containers = driver.find_elements(By.CLASS_NAME, "card-container")
        item_organizer(main_containers)
        next_page()
        break
    main_containers = driver.find_elements(By.CLASS_NAME, "card-container")
    item_organizer(main_containers)
