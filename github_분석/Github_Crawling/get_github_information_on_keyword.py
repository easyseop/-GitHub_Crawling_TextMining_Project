import time
import requests
import pandas as pd
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import urllib.request as ur


def search_information(name,page_n):

    df_dic = {}
    dic_keys = ['title','descript','topic_keyword','fork','star']
    
    url = 'https://github.com/orgs/{}/repositories?page={}'.format(name,page_n)

    html = ur.urlopen(url)
    soup = bs(html.read(), "html.parser")

    # 이름,별점,블로그,방문자 리뷰
    repository_list = soup.find_all("li", "Box-row") # 제목
    # print(len(repository_list)) # 한페이지당 30개의 repository가 존재 (full일 때)


    for k in dic_keys:
        df_dic[k] = []

    for repo in repository_list:
        title = repo.find('a','d-inline-block').text.strip() # 각 repository별 title 추출

        description = repo.find('p','color-fg-muted mb-0 wb-break-word') # 각 repository별 drcript 추출
        if description is not None:
            descript = description.text.strip()
        else:
            descript = '[BLANK]'

        topic_keyword = repo.find('div','d-inline-flex flex-wrap flex-items-center f6 my-1') #각 repository별 topic keyword 추출

        if topic_keyword is not None:
            topic_keyword_list = []
            for tk in topic_keyword.find_all('a'):
                topic_keyword_list.append(tk.text.strip())
        else:
            topic_keyword_list = []

        get_fork = repo.find('a','Link--muted mr-3') #각 repository별 fork 수 추출

        if get_fork is not None:
            fork = int(get_fork.text.strip().replace(',',''))
        else:
            fork = 0

        get_star = repo.find('a','no-wrap Link--muted mr-3') #각 repository별 star 수 추출

        if get_star is not None:
            star = int(get_star.text.strip().replace(',',''))
        else:
            star = 0


        df_dic['title'].append(title)
        df_dic['descript'].append(descript)
        df_dic['topic_keyword'].append(topic_keyword_list)
        df_dic['fork'].append(fork)
        df_dic['star'].append(star)



    return pd.DataFrame(df_dic)
