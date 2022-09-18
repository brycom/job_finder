from os import link
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:mmot_H3A_auW'
driver = webdriver.Chrome("C:\python\chromedriver.exe")
driver.get(url)


class MainContainersLocator:
    job_list = []
    main_containers = driver.find_elements(By.CLASS_NAME, 'card-container')
    print(main_containers.__len__())
    
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

intresting_link = MainContainersLocator.df["Ad link:"][1] 
intresting_ad = MainContainersLocator.df.iloc[1]
MainContainersLocator.df.to_csv("full_list_of_jobs.txt")
#print (intresting_ad)



driver.quit()


# //*[@id="tabpanel-0"]/pb-section-search-result/div/div/div/div/div/div/section/div/pb-feature-search-result-card[1]/div[2]/div[1]/h3/a