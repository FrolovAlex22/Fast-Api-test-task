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


def response_uri_training(URI: str):
    """Запрос к сервису"""
    # st_accept = "json"
    # st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    # headers = {
    #     "Accept": st_accept,
    #     "User-Agent": st_useragent
    # }

    query = """
    query MyQuery($priceGt: Float) {
      products(priceGt: $priceGt) {
        name
        price
        locations {
          name
        }
      }
    }
    """
    json_data = {
        'query': query,
        'variables': {
            'id': 138810,
        },
        'operationName': 'Product',
    }


    # operationName
    # :
    # "Product"
    # query
    # :
    # "query Product($id: ID!) {\n  product(id: $id) {\n    ...product\n    packageInListHotness\n    reviews(rows: 2, sortBy: \"rating\")
    # {\n      ...reviews\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment product on Product {\n  id\n  productId\n  itemId\n  slug\n  name\n  description\n  aiDescription\n  elevatorPitch\n  keyFeatures\n  compatibilityInfo\n  customLicense\n  rating {\n    average\n    count\n    __typename\n  }\n  currentVersion {\n    id\n    name\n    publishedDate\n    __typename\n  }\n  reviewCount\n  downloadSize\n  assetCount\n  publisher {\n    id\n    name\n    url\n    supportUrl\n    supportEmail\n    gaAccount\n    gaPrefix\n    __typename\n  }\n  mainImage {\n    big\n    facebook\n    small\n    icon\n    icon75\n    __typename\n  }\n  originalPrice {\n    itemId\n    originalPrice\n    finalPrice\n    isFree\n    discount {\n      save\n      percentage\n      type\n      saleType\n      __typename\n    }\n    currency\n    entitlementType\n    __typename\n  }\n  images {\n    type\n    imageUrl\n    thumbnailUrl\n    __typename\n  }\n  category {\n    id\n    name\n    slug\n    longName\n    __typename\n  }\n  firstPublishedDate\n  publishNotes\n  supportedUnityVersions\n  state\n  overlay\n  overlayText\n  plusProSale\n  licenseText\n  vspProperties {\n    ... on ExternalVSPProduct {\n      externalLink\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment reviews on Reviews {\n  count\n  canRate: can_rate\n  canReply: can_reply\n  canComment: can_comment\n  hasCommented: has_commented\n  totalEntries: total_entries\n  lastPage: last_page\n  comments {\n    id\n    date\n    editable\n    rating\n    user {\n      id\n      name\n      profileUrl\n      avatar\n      __typename\n    }\n    isHelpful: is_helpful {\n      count\n      score\n      __typename\n    }\n    subject\n    version\n    full\n    is_complimentary\n    vote\n    replies {\n      id\n      editable\n      date\n      version\n      full\n      user {\n        id\n        name\n        profileUrl\n        avatar\n        __typename\n      }\n      isHelpful: is_helpful {\n        count\n        score\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"

    # variables
    # :
    # {id: "138810"}

    query = """
    query Product($id: ID!) {
      product(id: $id) {
        id
        packageInListHotness
        }
      }

    """

    json_data = {
        'query': query,
        'variables': {
            'id': 138810,
        },
        'operationName': 'AddToCartButton',
    }

    response = requests.get(URI, json=json_data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


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
            result["title"] = text["name"]
            result["description"] = text["description"]
            return result

    return


if __name__ == "__main__":
    print(response_uri_training("https://assetstore.unity.com/api/graphql/batch"))
