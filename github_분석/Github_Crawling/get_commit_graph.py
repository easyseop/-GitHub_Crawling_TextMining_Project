
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
    print(url)
    driver = webdriver.Chrome(
            "/Users/seop/Documents/GitHub/-GitHub_Crawling_TextMining_Project/github_분석/Github_Crawling/chromedriver",
    chrome_options=chrome_options
        )
    driver.get(url)
    driver.implicitly_wait(15)

    bar_list = driver.find_elements(By.CLASS_NAME,'bar.mini')
    bar_list = [i.rect['height'] for i in bar_list]


    plt.figure(figsize=(20,10))
    plt.bar(range(1,len(bar_list)+1), bar_list)
    plt.title(f'{repo_name}-commit-activity', fontsize=20)
    plt.xlabel('date', fontsize=18)
    plt.ylabel('commits', fontsize=18)

    plt.savefig(f'./graph/{repo_name}_commit_graph.png')
