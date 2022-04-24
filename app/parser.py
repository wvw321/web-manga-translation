import requests
from bs4 import BeautifulSoup
from config import STATIC_FOLDER


class ParsPage:
    """Класс для считывания манги с страницы сайта"""

    def __init__(self, url: str = None, base_url: str = None, html_class: str = None, referer: str = None,
                 save_directory: str = None):
        """Инициализация класса"""
        self.url = url
        self.base_url = base_url
        self.html_class = html_class
        self.referer = referer
        self.save_directory = save_directory
        self.path_to_imgs = []

    def _get_html(self):
        """Получение HTML страницы в формате bs4"""
        self.html = BeautifulSoup(requests.get(self.url).text, 'html.parser')

    def _get_imgs_urls(self):
        """Получение ссылок на изображения"""
        self._get_html()
        selected = self.html.find('div', class_=self.html_class).select("img")
        self._urls_img = [selected[x].attrs["src"] for x in range(selected.__len__())]

    def _corect_url_simgs(self):
        """Добавление в адрес домен сайта """
        self._urls_img = [self.base_url + self._urls_img[x] for x in range(self._urls_img.__len__())]

    def get_imgs_data(self):
        """Сохранение изображений в переменной .imgs"""
        self._get_imgs_urls()
        ses = requests.session()
        if self.referer is not None:
            ses.headers.update({'referer': self.referer})

        if self.base_url is not None:
            self._corect_url_simgs()

        self.imgs = [ses.get(self._urls_img[x]).content for x in range(self._urls_img.__len__())]

    def save_imgs(self):
        """Сохранение изображений в файл"""
        if self.save_directory is not None:
            self.path_to_imgs.clear()

            for x in range(self.imgs.__len__()):
                directory = STATIC_FOLDER + self.save_directory + '/' + str(x) + '.jpg'
                img_file = open(directory, 'wb')
                img_file.write(self.imgs[x])
                img_file.close()
                self.path_to_imgs.append('/static' + self.save_directory + '/' + str(x) + '.jpg')





