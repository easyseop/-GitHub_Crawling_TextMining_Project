import time
import requests
import pandas as pd
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import *
from time import sleep
import warnings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

warnings.filterwarnings("ignore")

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

url = 'https://github.com/NVIDIA/NeMo/graphs/contributors'
driver = webdriver.Chrome(
            "./chromedriver",
    chrome_options=chrome_options
        )
driver.get(url)
driver.implicitly_wait(15)


get_con_info_list = driver.find_elements(By.CLASS_NAME,'d-block.Box') 
# get_con_info = driver.find_elements(By.CSS_SELECTOR,value=f'#contributors > ol > li:nth-child({i})').text.split() 반복문으로 
for i in get_con_info_list:
    con_info = i.text.split()
    rank = int(con_info[0].replace('#',''))
    name = con_info[1]
    commits = con_info[2]

    print(rank,name,commits)
    print()

driver.quit()
print('done')