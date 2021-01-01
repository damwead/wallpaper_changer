from bs4 import BeautifulSoup
import requests
import lxml


headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) "
                         "AppleWebKit/537.75.14 (KHTML, like Gecko) "
                         "Version/7.0.3 Safari/7046A194A"}
url = 'https://www.reddit.com/r/wallpaper/top/?t=day'


html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')


images_tags = soup.find_all('img', class_='media-element')
posts_names = soup.find_all('h3', class_='_eYtD2XCVieq6emjKBH3m')


images_names = []
images_ids = []

for i in range(len(images_tags)):
    if images_tags[i]['src'][23] == '/':
        images_ids.append(images_tags[i]['src'][24:41])
        if posts_names[i].text[-5:-1].isalnum():
            images_names.append(posts_names[i].text)


for image in range(len(images_ids)):
    image_url = "https://i.redd.it/" + str(images_ids[image])  # image = pic_name.png or pic_name.jpg
    print(image_url)

    response_img = requests.get(image_url, headers=headers)

    print(images_names[image]+images_ids[image][-4:])

    image = open(images_names[image]+images_ids[image][-4:], 'wb')
    image.write(response_img.content)
    image.close()

