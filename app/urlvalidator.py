import validators.url
from urllib.parse import urlparse
from constants import SITE_LIST


def url_check(url: str):
    if validators.url(url):
        host_name = urlparse(url).hostname
        for key in SITE_LIST:
            if host_name == key:
                config = SITE_LIST.get(key)
                config.update(url=url)
                return True, config
        return False, 'Данный сайт не поддерживается '
    else:
        return False, 'Некоректный url адресс'

