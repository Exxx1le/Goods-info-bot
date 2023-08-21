import re

from constants import SUPPORTED_SHOPS


def link_checker(user_url) -> str:
    try:
        if re.match(
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?", str(user_url)
        ):
            link_list = str(user_url).split("/")
            if link_list[2] in SUPPORTED_SHOPS:
                return link_list[2]
            else:
                return False
    except IndexError as e:
        return "Not a link"
