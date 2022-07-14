import time
from unittest import result
from get_github_repository_contributor import get_contributor

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
    