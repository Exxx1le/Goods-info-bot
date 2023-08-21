import requests
from bs4 import BeautifulSoup


def gold_apple_stock_status(user_url):
    response = requests.get(f"{user_url}")
    soup = BeautifulSoup(response.text, "html.parser")
    add_to_cart_button = soup.findAll(
        attrs={"class": "button-primary button-primary_add-to-cart"}
    )
    print(add_to_cart_button)
    for title in add_to_cart_button:
        if title.text.strip() == "Добавить в корзину":
            return True
        elif title.text.strip() == "Узнать о поступлении":
            return False


print(gold_apple_stock_status("https://goldapple.ru/19000126321-almost-lipstick"))
