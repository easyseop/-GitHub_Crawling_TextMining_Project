
import time
from get_commit_graph import get_commits_graph
from get_github_repository_contributor import get_contributor
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import os
import threading

def search_title(name,page_n):
    
    lis = []
    
    url = 'https://github.com/orgs/{}/repositories?page={}'.format(name,page_n)

    html = ur.urlopen(url)
    soup = bs(html.read(), "html.parser")

    # 이름,별점,블로그,방문자 리뷰
    repository_list = soup.find_all("li", "Box-row") # 제목
    
    for repo in repository_list:
        title = repo.find('a','d-inline-block').text.strip()
        
        lis.append(title)
        
    return lis

def get_repo_name(name):
    title_list =[]
    for i in range(9,11+1): # 한 개의 루프 당 30개 레포지토리 크롤링 
        print(i)
        temp_lis = search_title(name,i)
        title_list+=temp_lis
    return title_list


def get_urls(cor_name,repo_name):
    url = f'https://github.com/{cor_name}/{repo_name}/graphs/commit-activity'

    return url,repo_name



def main(cor_name):
    urls = []
    repo_name_list = get_repo_name(cor_name)
    
    for repo_name in repo_name_list:
        url,repo_name = get_urls(cor_name,repo_name)
        urls.append(url)
    executor = ProcessPoolExecutor(max_workers=10)
    result_rivew = list(executor.map(get_commits_graph, urls,repo_name_list))
    return result_rivew

if __name__ == '__main__':

    dir_name ="graph" 
    try:
        os.mkdir(dir_name)
    except:
        pass
    start = time.time()
    re = main('NVIDIA')
    print(re)
    end = time.time()
    print(end-start)