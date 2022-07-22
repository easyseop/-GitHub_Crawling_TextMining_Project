import time
from get_github_information_on_keyword import search_information
import requests
import pandas as pd
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import urllib.request as ur

def main(name):

    df = pd.DataFrame(
            columns=[
                "title",
                "descript",
                "topic_keyword",
                "fork",
                "star",
            ]
        )

    for i in range(1,15): # 한 페이지당 repo 30개씩 추출 가능 
        temp_df = search_information(name,i)

        df = pd.concat([df,temp_df],ignore_index=True)
    return df


if __name__ == "__main__":

    start = time.time()
    result_df = main('NVIDIA')
    result_df.to_csv('test_repo_info.csv',encoding = 'utf-8')
    end = time.time()
    print(result_df)
    print(end - start, " second")
