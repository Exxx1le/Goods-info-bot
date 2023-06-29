SUPPORTED_SHOPS = {"goldapple.ru": "Золотое яблоко"}


def link_checker(user_url):
    try:
        link_list = str(user_url).split("/")
        if link_list[0] == "https:" or link_list[0] == "http":
            if link_list[2] in SUPPORTED_SHOPS:
                return link_list[2]
        else:
            return False
    except IndexError as e:
        return "Not Link"
