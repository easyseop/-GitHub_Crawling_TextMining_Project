#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from RISC_V_Exchange_Software import search_software_url
from tqdm import tqdm


# In[3]:


url_and_repo_name = search_software_url()
url_and_repo_name


# In[5]:


for url,repo_name in tqdm(url_and_repo_name):
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    software_type_url = url

    browser.get(url)

    prev_height = browser.execute_script("return document.body.scrollHeight")

    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # 페이지 로딩 대기
        time.sleep(2)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script("return document.body.scrollHeight")

        if(curr_height == prev_height):
            break
        else:
            prev_height = browser.execute_script("return document.body.scrollHeight")



    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'lxml')


    str_software_name = []
    software_list = soup.find_all("div", "col-results span_2_of_3-results")

    
    dic = {}
    dic['Topic'] = []
    dic['Description'] = []
    dic['Organization'] = []
    dic['License Type'] = []
    dic['Software Type'] = []


    for sw in software_list:

        topic_name = sw.find('h2','results-title').text.strip()
        dic['Topic'].append(topic_name)


        text,org_name,lic_name,sw_name = None,None,None,None

        tag_name_list = sw.find_all('p')

        if tag_name_list is not None: # p 태그가 한 개라도 존재한다면
            for tg in tag_name_list:


                if len(tg.text.split(':')) == 1:
                    text = tg.text

                else:
                    tag_name,tag_value = tg.text.split(':')


                    if tag_name == 'Organization':
                        org_name = tag_value
                    elif tag_name == 'Software Type':
                        sw_name = tag_value
                    else:
                        lic_name = tag_value

            dic['Description'].append(text)
            dic['Organization'].append(org_name)
            dic['License Type'].append(lic_name)
            dic['Software Type'].append(sw_name)
            
            result_df = pd.DataFrame(dic)
            result_df.to_csv(f'Risc_v_{repo_name}_info.csv',encoding = 'utf-8')
    


# In[ ]:


#     dic = {}
#     dic['Topic'] = []
#     dic['Description'] = []
#     dic['Organization'] = []
#     dic['License Type'] = []
#     dic['Software Type'] = []


#     for sw in software_list:

#         topic_name = sw.find('h2','results-title').text.strip()
#         dic['Topic'].append(topic_name)


#         text,org_name,lic_name,sw_name = None,None,None,None

#         tag_name_list = sw.find_all('p')

#         if tag_name_list is not None: # p 태그가 한 개라도 존재한다면
#             for tg in tag_name_list:


#                 if len(tg.text.split(':')) == 1:
#                     text = tg.text

#                 else:
#                     tag_name,tag_value = tg.text.split(':')


#                     if tag_name == 'Organization':
#                         org_name = tag_value
#                     elif tag_name == 'Software Type':
#                         sw_name = tag_value
#                     else:
#                         lic_name = tag_value

#             dic['Description'].append(text)
#             dic['Organization'].append(org_name)
#             dic['License Type'].append(lic_name)
#             dic['Software Type'].append(sw_name)
            
#             pd.DataFrame(dic)


# In[ ]:




