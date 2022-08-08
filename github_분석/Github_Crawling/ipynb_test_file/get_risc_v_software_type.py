#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import urllib.request as ur
import warnings
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def search_software_url():
        #url 링크 따와서 고정적인 부분 나두고 변경되는 소프트웨어 타입 이름들 리스트에 넣어서 반복문 돌림
    #
    #돌려가면서 나오는 자료내용들 추출
    url_1 = 'https://riscv.org/exchange/?_sft_exchange_category=software'
    html = ur.urlopen(url_1)
    soup = bs(html.read(), "html.parser")

    software_type_list = soup.find_all("ul", {'data-operator':'or'}) # 제목

    
    df_dic = []
    for i in software_type_list[13].find_all('li',"sf-level-0" ):
        title = i.text.strip()

        df_dic.append(title)
    
    url_and_repo_name = []
    BASE_URL = 'https://riscv.org/exchange/?_sft_exchange_category=software&_sfm_exchange_software_type='
    
    
    for i in tqdm(df_dic):
        url = BASE_URL
        string = i.split()

        for j in string:
            if j == string[-1]:
                url+=j
            else:
                url+= (j+'%20')
        url_and_repo_name.append([url,i]) 
        
    return url_and_repo_name


# In[ ]:




