import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd

df = pd.read_csv('data.csv')

usr = "" #insert your username here
pwd = "" #insert your password here

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1420,1080')

url = "https://www.tradingview.com"
chrome_executable = Service(executable_path='/usr/local/bin/chromedriver', log_path='NUL')
driver = webdriver.Firefox()#  webdriver.Chrome(service=chrome_executable)

# time.sleep(600)
driver.get(url)

time.sleep(1)
driver.page_source
if driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/button[1]'):
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/button[1]').click()

time.sleep(3)
driver.page_source
if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]'):
    driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]').click()

time.sleep(1)
if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span'):
    driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()

elem = driver.find_element(By.NAME,"username")
elem.send_keys(usr)

elem = driver.find_element(By.NAME,"password")
elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)
time.sleep(2)

url = "https://www.tradingview.com/chart"
driver.get(url)

time.sleep(1)
driver.page_source
try:
    if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div[2]'):
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div[2]').click()
except:
    pass

for x in df.index:
    time.sleep(1)
    url = f"""https://www.tradingview.com/chart/?symbol=MYX%3A{df['symbol_name'][x]}"""
    driver.get(url)

    time.sleep(1)
    driver.page_source
    if driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[2]/div/div/div/div/div[2]'):
        driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[2]/div/div/div/div/div[2]').click()

    time.sleep(2)
    driver.page_source
    if driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]'):
        driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]').click()

    time.sleep(2)
    driver.page_source
    if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div[1]/div/div/p/form/fieldset/div[2]/span/span/span[1]/span'):
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div[1]/div/div/p/form/fieldset/div[2]/span/span/span[1]/span').click()

    time.sleep(1)
    driver.page_source
    if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div[1]/div/div/p/form/fieldset/div[2]/span/span/span[2]/span/span/span[5]/span'):
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div[1]/div/div/p/form/fieldset/div[2]/span/span/span[2]/span/span/span[5]/span').click()

    elem = driver.find_element(By.NAME,"band-additional")
    elem.send_keys([Keys.BACKSPACE] * 1000)
    print(elem.get_attribute("value"))
    elem.send_keys(df['ep'][x])

    time.sleep(1)
    driver.page_source
    if driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[3]/div[2]'):
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[3]/div[2]').click()

    time.sleep(1)
    driver.page_source
    if driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[2]/div/div/div/div/div[2]'):
        driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div/div[2]/div/div/div/div/div[2]').click()



