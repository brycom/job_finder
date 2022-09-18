from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:mmot_H3A_auW'
driver = webdriver.Chrome("C:\python\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(2)
#decline cookiea
decline_button = driver.find_element(By.ID , 'afCookieDecline')
decline_button.click()
#get adds at first page
driver.implicitly_wait(2)
#change page and get adds until number of adds are les then max
next_button = driver.find_element(By.XPATH ,"/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH ,"/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button"))
    )
    next_button.click()
except:
    driver.quit()


next_button = driver.find_element(By.XPATH ,"/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-search/div[2]/pb-feature-tabs/div[2]/pb-section-search-result/div/div/div/div/div/div/pb-feature-pagination/digi-navigation-pagination/div/nav/digi-button[2]/button")
next_button.click()


#driver.quit()
