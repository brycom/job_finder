import pandas as pd
from platsbanken.Elements import CheckAds, discard, interesting, maybe
from platsbanken.Page import driver, job_list, runging_page

runging_page()


for i in job_list:
    url = i["Ad link:"]
    driver.get(url)
    run_ad = CheckAds()
    run_ad.BaseCriterias(i)
    run_ad.Suitebilety(i)

df_interesting = pd.DataFrame(interesting)
df_maybe = pd.DataFrame(maybe)
df_discard = pd.DataFrame(discard)
df_interesting.style.set_properties(**{"border": "2px solid white"})
df_interesting.style.bar()


print(f"interesting: {df_interesting}")
print(f"maybe:{df_maybe}")
print(f"not interesting: {df_discard}")
html = df_interesting.to_html(), df_maybe.to_html()
print(html)


# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# from config import password, username
# from linkedin.login import LogIn

# run = LogIn(username, password)
# run.enter_credentiols()
