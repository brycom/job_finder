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


print(f"interesting: {df_interesting}")
print(f"maybe:{df_maybe}")
print(f"not interesting: {df_discard}")

driver.quit()
