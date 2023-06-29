import requests
from bs4 import BeautifulSoup

supported_shops = {"goldapple.ru": "Золотое яблоко"}


def link_checker(user_url):
    try:
        link_list = str(user_url).split("/")
        if link_list[0] == "https:" or link_list[0] == "http":
            if link_list[2] in supported_shops:
                return link_list[2]
        else:
            return False
    except IndexError as e:
        return "Not Link"


def gold_apple_stock_status(user_url):
    response = requests.get(f"{user_url}")
    soup = BeautifulSoup(response.text, "html.parser")
    add_to_cart_button = soup.findAll(
        attrs={"class": "button-primary button-primary_add-to-cart"}
    )

    for title in add_to_cart_button:
        if title.text.strip() == "Добавить в корзину":
            return True
        elif title.text.strip() == "Узнать о поступлении":
            return False
