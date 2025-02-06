import json

from bs4 import BeautifulSoup
import requests


URI_FREE = "https://assetstore.unity.com/search#nf-ec_price_filter=0...0"
URI_BY_ID = "https://assetstore.unity.com/packages/packages/"


def response_uri(URI: str):
    """Запрос к сервису"""
    st_accept = "json"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }
    response = requests.get(URI, headers)

    if response.status_code == 200:
        return response.text
    else:
        return response.status_code


def parsing_response_free():  # Не смог реализовать
    """Парсинг бесплатных продуктов"""
    free_result = response_uri(URI_FREE)
    soup = BeautifulSoup(free_result, 'lxml')

    return soup.title.text


async def parsing_response_by_id(id: str):
    """Парсинг ответа продукта по id"""
    result = {}
    NEW_URI = f"{URI_BY_ID}{id}"

    response = response_uri(NEW_URI)
    soup = BeautifulSoup(response, 'lxml')

    for scrypt in soup("script"):
        if scrypt.has_attr("type") and scrypt["type"] == "application/ld+json":
            text = json.loads(scrypt.text)
            result["name"] = text["name"]
            result["description"] = text["description"]
            return result

    return
