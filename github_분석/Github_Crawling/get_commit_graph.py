
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import warnings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def get_commits_graph(url,repo_name):
    from collections import defaultdict
    dic = defaultdict(list)
    dic['repo_name'].append(repo_name)

    driver = webdriver.Chrome(
            "/Users/seop/Documents/GitHub/-GitHub_Crawling_TextMining_Project/github_분석/Github_Crawling/chromedriver",
    chrome_options=chrome_options
        )
    driver.get(url)
    driver.implicitly_wait(15)

    bar_list = driver.find_elements(By.CLASS_NAME,'bar.mini')
    xaxis = driver.find_elements(By.CLASS_NAME,'x.axis')
    bar_list = [i.rect['height'] for i in bar_list]

    bar_scaling = []

    if bar_list:

        minimum = min([i for i in bar_list if i!= 0])
        
        for index,bl in enumerate(bar_list,start=1):
            score = bl//minimum
            bar_scaling.append(score)
            dic[index].append(score)
    # print(dic,'sksrp')
    return dic








    
        
    # if xaxis:
    #     x_ticks = xaxis[0].text.split('\n')
    #     new_xticks= [] 
    #     for x in x_ticks:
    #         new_xticks.append(x)
    #         new_xticks.append('')
    #         new_xticks.append('')
    # else:
    #     new_xticks= []
    # plt.figure(figsize=(20,10))
    # plt.bar(range(1,len(bar_scaling)+1), bar_scaling)
    
    # plt.title('commit-activity', fontsize=20)
    # plt.xticks(range(0,len(new_xticks)), new_xticks)

    # plt.xlabel('date', fontsize=18)
    # plt.ylabel('commits', fontsize=18)
