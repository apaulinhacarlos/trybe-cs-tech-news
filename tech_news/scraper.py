import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)

    next_btn = "main a.tec--btn::attr(href)"
    next_page = selector.css(next_btn).get()
    return next_page


# print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))

# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("main h1.tec--article__header__title::text").get()
    timestamp = selector.css("main time::attr(datetime)").get()

    writer = (
        selector.css("main div.tec--author__info *::text").get()
        or selector.css("main div.tec--timestamp__item a::text").get()
    ).strip() or None

    shares_count = int(
        selector.css("main div.tec--toolbar__item::text").re_first(r"\d+") or 0
    )

    comments_count = int(
        selector.css("main button.tec--btn::text").re_first(r"\d+")
    )

    summary = selector.css(
        "main div.tec--article__body p:first-child *::text"
    ).getall()
    summary = "".join(summary)

    sources = selector.css("div.z--mb-16 h2 ~ div a.tec--badge::text").getall()
    sources = [source.strip() for source in sources]

    categories = selector.css("main a.tec--badge--primary::text").getall()
    categories = [category.strip() for category in categories]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# print(
#     scrape_noticia(
#         fetch(
#             "https://www.tecmundo.com.br/minha-serie/215330-8-series-parecidas-the-crown-fas-realeza.htm"
#         )
#     )
# )


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(URL)
    news_url_list = scrape_novidades(html_content)

    while len(news_url_list) < amount:
        next_page = scrape_next_page_link(html_content)
        html_content = fetch(next_page)
        news_url_list.extend(scrape_novidades(html_content))

    news_url_list = news_url_list[:amount]

    scraped_news = []
    for news in news_url_list:
        news_html_content = fetch(news)
        scraped_new = scrape_noticia(news_html_content)
        scraped_news.append(scraped_new)

    create_news(scraped_news)
    return scraped_news


# get_tech_news(3)
