import requests
from bs4 import BeautifulSoup

URL = 'https://animevost.org/page/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="shortstory")
    news = []
    for item in items:
        if item.find("td").find("h4") is not None:
            news.append({
                "title": item.find("td").find("h4").getText(),
                "link": item.find("div", class_="shortstoryHead").find('a').get("href"),
            })
    return news

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = get_data(html.text)
        return anime
    else:
        raise Exception("Error!")