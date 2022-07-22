# import time
# import requests
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# import warnings
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# warnings.filterwarnings("ignore")
# def get_contributor(url):

#     df_dic = {} 
#     df_dic['rank'] = []
#     df_dic['name'] = []
#     df_dic['commits'] = []

#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--headless")

#     driver = webdriver.Chrome(
#                 "./chromedriver",
#         chrome_options=chrome_options
#             )
#     driver.get(url)
#     driver.implicitly_wait(15)


#     get_con_info_list = driver.find_elements(By.CLASS_NAME,'d-block.Box') 
#     # get_con_info = driver.find_elements(By.CSS_SELECTOR,value=f'#contributors > ol > li:nth-child({i})').text.split() 반복문으로 
#     for i in get_con_info_list:
#         con_info = i.text.split()
#         rank = int(con_info[0].replace('#',''))
#         name = con_info[1]
#         commits = con_info[2]

#         df_dic['rank'].append(rank)
#         df_dic['name'].append(name)
#         df_dic['commits'].append(commits)
    
#     df = pd.DataFrame(df_dic)
#     print('done')
#     return df
    
   
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import warnings
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

def get_contributor(url,repo_name):

    df_dic = {} 
    df_dic['rank'] = []
    df_dic['name'] = []
    df_dic['commits'] = []


    driver = webdriver.Chrome(
                "/Users/seop/Documents/GitHub/-GitHub_Crawling_TextMining_Project/github_분석/Github_Crawling/chromedriver",
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

        df_dic['rank'].append(rank)
        df_dic['name'].append(name)
        df_dic['commits'].append(commits)
    
    df = pd.DataFrame(df_dic)
    df.to_csv(f'NVIDIA_{repo_name}_contributors_multiprocessing.csv',encoding='utf-8-sig',index=False)
    print('done')
