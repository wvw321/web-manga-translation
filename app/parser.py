import requests
from bs4 import BeautifulSoup


class ParsPage:
    """Класс для считывания манги с страницы сайта"""

    def __init__(self, url: str, html_class: str, referer: str):
        """Инициализация класса"""
        self.url = url
        self.html_class = html_class
        self.referer = referer

    def _get_html(self):
        """Получение HTML страницы в формате bs4"""
        self.html = BeautifulSoup(requests.get(url).text, 'html.parser')

    def get_imgs_urls(self):
        """Получение ссылок на изображения"""
        self._get_html()
        selected = self.html.find('div', class_=self.html_class).select("img")
        self._urls_img = [selected[x].attrs["src"] for x in range(selected.__len__())]

    def get_imgs_data(self):
        """Схранение изображений в переменной .imgs"""
        ses = requests.session()
        ses.headers.update({'referer': self.referer})
        self.imgs = [ses.get(self._urls_img[x]).content for x in range(self._urls_img.__len__())]

    def corect_url_simgs(self, editor: str):
        """Добавление в адрес домен сайта """
        self._urls_img = [editor + self._urls_img[x] for x in range(self._urls_img.__len__())]
