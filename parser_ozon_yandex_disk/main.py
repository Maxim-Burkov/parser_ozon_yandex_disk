import requests
from bs4 import BeautifulSoup

from config import HEADERS

def start():
    get_url(input('Введите url: '))

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# парсинг
def parse(url):
    r = requests.Request()
    # div, class_='r6j rj8 js'
    # span, class_='rj7 jr8'

# проверка url
def check_url(url):
    if 'https://www.ozon.ru/' not in url:
        print('Ошибка: введенная вами ссылка с другого сайта. Повторите попытку')
        start()
    else:
        html = get_html(url)
        if html.status_code == 200:
            print('Все ок, начинаем парсить')
            return parse(html)
        else:
            print('Ошибка: ', html.status_code)


# получаем url
def get_url(url):
    check_url(url)

if __name__ == '__main__':
    start()
