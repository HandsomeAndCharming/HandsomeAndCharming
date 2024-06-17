import requests
from bs4 import BeautifulSoup

def scrape_xiaohongshu(keyword):
    url = f'https://www.xiaohongshu.com/search?keyword={keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('div', class_='post')
    for post in posts:
        title = post.find('h1').get_text()
        description = post.find('p').get_text()
        print(f'Title: {title}\nDescription: {description}\n')

if __name__ == "__main__":
    keyword = '亲子游'
    scrape_xiaohongshu(keyword)
