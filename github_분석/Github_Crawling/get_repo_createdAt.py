from collections import defaultdict
import requests
import pandas as pd
import numpy as np
import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs
import urllib.request as ur
def search_information(name,page_n):
    
    
    df_dic = {}
    dic_keys = ['title']
    
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
        df_dic['title'].append(title)

        
    return pd.DataFrame(df_dic)


def get_titles(name):

    df = pd.DataFrame(
            columns=[
                "title",
                "descript",
                "topic_keyword",
                "fork",
                "star",
            ]
        )

    for i in range(1,16):
        temp_df = search_information(name,i)

        df = pd.concat([df,temp_df],ignore_index=True)
    return df



async def fetch(session,url,repo_name):
    # print(url)
    headers = { "Authorization": "token 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"}
    async with session.get(url, headers=headers) as response:
        res = await response.json()  # json으로 호출
        create_date = res.get('created_at')
        # print(repo_name,create_date)
        dic['repo_name'].append(repo_name)
        dic['create_date'].append(create_date.split('T')[0])


async def main():

    titles = get_titles('NVIDIA')
    urls = [[i,f"https://api.github.com/repos/nvidia/{i}"] for i in titles['title']]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url,repo_name) for repo_name, url in urls])

s = time.time()
dic = {'repo_name':[] , 'create_date':[]}
asyncio.run(main())
print('learning time : ',time.time()-s)
df = pd.DataFrame(dic)


df.to_csv('repo_createAt.csv')