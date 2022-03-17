from tech_news.database import search_news
from datetime import datetime


# Requisito 6
# Ignorar case sensitive
# https://stackoverflow.com/questions/1863399/mongodb-is-it-possible-to-make-a-case-insensitive-query
def search_by_title(title):
    news_list_by_title = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )

    news_search_by_title = []
    for news in news_list_by_title:
        news_search_by_title.append((news["title"], news["url"]))

    return news_search_by_title


# print(search_by_title("pluto"))


# Requisito 7
# valida data
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    try:
        if date == datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d"):
            news_list_by_date = search_news({"timestamp": {"$regex": date}})

            news_search_by_date = []
            for news in news_list_by_date:
                news_search_by_date.append((news["title"], news["url"]))

            return news_search_by_date
    except ValueError:
        raise ValueError("Data inválida")


# print(search_by_date("20-11-2023"))


# Requisito 8
def search_by_source(source):
    news_list_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )

    news_search_by_source = []
    for news in news_list_by_source:
        news_search_by_source.append((news["title"], news["url"]))

    return news_search_by_source


# print(search_by_source("ResetERA"))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
