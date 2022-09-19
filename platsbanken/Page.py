from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


url = 'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:mmot_H3A_auW'
driver = webdriver.Chrome("C:\python\chromedriver.exe")
driver.get(url)

#list for pd dataframe.
job_list = []

#Decline cookis.
decline_button = driver.find_element(By.ID , 'afCookieDecline')
decline_button.click()

#Locate main containers.
main_containers = driver.find_elements(By.CLASS_NAME, 'card-container')

#Locate and puch the next button.

try:
    element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located(By.XPATH ,'/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button/span[1]/span')
    )
except:
    driver.quit()

next_button = driver.find_element(By.XPATH ,'/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button/span[1]/span')
next_button.click()


# Apend secend pages maincontainers.
main_containers.append( driver.find_elements(By.CLASS_NAME, 'card-container'))

print("Number of main containers " , main_containers.__len__())

#Compaile the list for pd dataframe
for i in main_containers:
    job_ad = i.find_element(By.TAG_NAME , "a")
    ad_link = job_ad.get_attribute('href')
    job_description = job_ad.text
    company_and_city = i.find_element(By.CLASS_NAME, 'pb-company-name').text
    
    job_items = {
        'Company and City:' : company_and_city,
        'Job description:': job_description ,
        'Ad link:': ad_link
    }
        
    job_list.append(job_items)



df = pd.DataFrame(job_list)
print(df)


#intresting_link = MainContainersLocator.df["Ad link:"][1] 
#intresting_ad = MainContainersLocator.df.iloc[1]
#MainContainersLocator.df.to_csv("full_list_of_jobs.txt")
#print (intresting_ad)



driver.quit()


