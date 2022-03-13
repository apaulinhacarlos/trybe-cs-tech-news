import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# print(fetch("http://httpbin.org/status/404"))
# print(fetch("http://httpbin.org/delay/5"))


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    url_list = []
    news_url_selector = "main a.tec--card__title__link::attr(href)"
    for url in selector.css(news_url_selector).getall():
        url_list.append(url)

    if len(url_list) == 0:
        return []
    return url_list


# print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
