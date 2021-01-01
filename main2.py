from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"}
url = 'https://www.reddit.com/r/wallpaper/top/?t=day'


html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')

with open('html_text_file.html', 'w') as f:
    f.write(html_text)


def get_clean_html_code():
    html_file = soup.prettify()
    with open('html_file_orig.html', 'w') as f:
        for i in html_file:
            f.write(i)

    with open('html_file.html', 'r') as f_read:
        lines = f_read.readlines()

    with open('html_file.html', 'w') as f:
        for line in lines:
            if '<' in line:
                f.write(line)


posts = soup.find_all('div', class_='scrollerItem')


for post in posts:
    # find objects in posts
    post_name = post.find('h3', class_='_eYtD2XCVieq6emjKBH3m').text
    date = post.find('div', class_='cZPZhMe-UCZ8htPodMyJ5').a.text
    img = post.find('img', class_='media-element')

    print(f'''
    Post name: {post_name}
    Posted: {date}
    IMG: {img}
    ''')
    print('')

