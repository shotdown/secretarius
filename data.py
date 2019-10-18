import requests, re
from bs4 import BeautifulSoup

url ='https://ria.ru/world/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
contents = soup.find_all(class_='list-item__content')
images = soup.find_all(class_='list-item__image')
texts = []
images_ref = []
links = []

def newsLinks():
    for i in range(len(contents)):
        texts.append(contents[i].get_text())
        
        link = re.findall('href=[\"a-zA-Z0-9:/._]*',
                            str(contents[i]))[0].replace('href=', '').replace('"', '')
        links.append(link)

    return links
