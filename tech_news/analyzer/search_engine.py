from pyparsing import Regex
from tech_news.database import search_news


# Requisito 6
# Ignorar case sensitive
# https://stackoverflow.com/questions/1863399/mongodb-is-it-possible-to-make-a-case-insensitive-query
def search_by_title(title):
    newsList = search_news({"title": {"$regex": title, "$options": "i"}})

    newsSearchByTitle = []
    for news in newsList:
        newsSearchByTitle.append((news["title"], news["url"]))

    return newsSearchByTitle


# print(search_by_title("pluto"))


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
