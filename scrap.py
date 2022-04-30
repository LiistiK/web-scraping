import requests
import bs4
from heads import HEADERS

KEYWORDS = ['IT-компании', 'web', 'python']
url = 'https://habr.com/ru/all/'
ret = requests.get(url, headers= HEADERS)
text = ret.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = url + href
            title = article.find('h2').find('span').text
            result = f"Статья - {title} доступна по ссылке {link}"
            print(result)