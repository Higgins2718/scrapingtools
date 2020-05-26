import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib
import urllib.request
import requests
http = httplib2.Http()
status, response = http.request('https://pmarchive.com')


def get_post(url, file):
    print("GET", url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    post_content = soup.find_all('div', attrs={"class":"post_content"})
    filename = file.split('.html')[0]
    if post_content is not None:
        text = ""
        for i in post_content:
            text = i.text
            print(text)
        try:
            with open('post_text/'+filename+".txt", "w") as file:
                file.write(text)
                # Uncomment to download raw html of post
                # file.write(str(post_content))

        except Exception:
            pass


for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print('https://pmarchive.com/'+link['href'], link['href'])
        get_post('https://pmarchive.com/'+link['href'], link['href'])
# Uncomment to download individual post
# get_post('https://pmarchive.com/guide_to_personal_productivity.html', 'guide_to_personal_productivity.html')
