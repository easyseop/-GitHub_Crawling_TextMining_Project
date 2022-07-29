#!/usr/bin/env python
# coding: utf-8

# In[39]:


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


url_1 = 'https://riscv.org/exchange/?_sft_exchange_category=software'
html = ur.urlopen(url_1)
soup = bs(html.read(), "html.parser")

software_type_list = soup.find_all("ul", {'data-operator':'or'}) # 제목


df_dic = []
for i in software_type_list[13].find_all('li',"sf-level-0" ):
    title = i.text.strip()

    df_dic.append(title)


# In[40]:


df_list = []
for i in df_dic:
    df = pd.read_csv('./RISC_V_Software_type_info/Risc_v_{}_info.csv'.format(i))
    df_list.append(df)
    
plus = pd.concat(df_list)


# In[41]:


df_plus = pd.DataFrame(plus['Organization'])


# In[42]:


list_df_plus = df_plus.values.tolist()


# In[43]:


import itertools

list_plus = list(itertools.chain(*list_df_plus))


# In[44]:


list_plus


# In[45]:


from collections import Counter


# In[46]:


count_items = Counter(list_plus)
print(count_items)


# In[ ]:




