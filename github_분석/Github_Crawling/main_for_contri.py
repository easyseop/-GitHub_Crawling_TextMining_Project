import time
from unittest import result
from get_github_repository_contributor import get_contributor


def search_title(name,page_n):
    
    df_dic = []
    
    url = 'https://github.com/orgs/{}/repositories?page={}'.format(name,page_n)

    html = ur.urlopen(url)
    soup = bs(html.read(), "html.parser")

    # 이름,별점,블로그,방문자 리뷰
    repository_list = soup.find_all("li", "Box-row") # 제목
    
    for repo in repository_list:
        title = repo.find('a','d-inline-block').text.strip()
        
        df_dic.append(title)
        temp_df = df_dic
        
    return temp_df

def main(name):
    title_list =[]
    for i in range(1,11):
        temp_df = search_title(name,i)
        title_list.append(temp_df)
    return title_list


def main(cor_name,repo_name):
    url = f'https://github.com/{cor_name}/{repo_name}/graphs/contributors'
    dataframe = get_contributor(url)
    return dataframe


if __name__ == "__main__":

    start = time.time()
    result_df = main('NVIDIA','NeMo')
    end = time.time()
    result_df.to_csv('test_contributor.csv',index=False,encoding = 'utf-8')
    print(end - start, " second")
    