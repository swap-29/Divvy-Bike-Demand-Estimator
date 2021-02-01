from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

dfs = []
for d in range(1, 32):
    date = '2020-8-' + str(d)
    url = 'https://www.wunderground.com/history/daily/KMDW/date/' + date
    driver = webdriver.Chrome()
    driver.get(url)

    tables = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-table.cdk-table.mat-sort.ng-star-inserted")))
    for table in tables:
        newTable = pd.read_html(table.get_attribute('outerHTML'))
        if newTable:
            df = newTable[0].fillna('')
            # df.reset_index(drop=True)
            df['Date'] = date
            date_col = df.pop('Date')
            df.insert(0, "Date", date_col)
            dfs.append(df)

            print("DATE: ", date)
            print(df)
        driver.close()

            # print(type(newTable[0]))

    merged = pd.concat(dfs)
    merged.to_csv('Aug2020.csv', index=False)



