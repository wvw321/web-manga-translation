import requests
from bs4 import BeautifulSoup


class ParsPage:
    """Класс для считывания манги с страницы сайта"""

    def __init__(self, url: str, html_class: str, referer: str):
        """Инициализация класса"""
        self.url = url
        self.html_class = html_class
        self.referer = referer

    def __gethtml(self):
        """Получение HTML страницы в формате bs4"""
        self.html = BeautifulSoup(requests.get(url).text, 'html.parser')

    def geturlsimgs(self):
        """Получение ссылок на изображения"""
        self.__gethtml()
        selected = self.html.find('div', class_=self.html_class).select("img")
        self._urls_img = [selected[x].attrs["src"] for x in range(selected.__len__())]

    def getimgs(self):
        """Схранение изображений в переменной .imgs"""
        ses = requests.session()
        ses.headers.update({'referer': self.referer})
        self.imgs = [ses.get(self._urls_img[x]).content for x in range(self._urls_img.__len__())]

    def corecturlsimgs(self, editor: str):
        """Добавление в адрес домен сайта """
        self._urls_img = [editor + self._urls_img[x] for x in range(self._urls_img.__len__())]


def readmanganatoParser(url: str):
    if type(url) != str:
        raise ValueError
    page = requests.get(url)
    page_bs4 = BeautifulSoup(page.text, 'html.parser').find('div', class_="container-chapter-reader").select("img")
    urls_img = [page_bs4[x].attrs["src"] for x in range(page_bs4.__len__())]
    referer = "https://readmanganato.com/"
    ses = requests.session()
    ses.headers.update({'referer': referer})
    imgs = [ses.get(urls_img[x]).content for x in range(urls_img.__len__())]

    return imgs


def saveImg(imgs: list):
    for x in range(imgs.__len__()):
        der = 'B:/Data/' + str(x) + '.jpg'
        img_file = open(der, 'wb')
        img_file.write(imgs[x])
        img_file.close()


if __name__ == "__main__":
    url = "https://readmanganato.com/manga-dg980989/chapter-140"
    url = "https://www.readm.org/manga/20929/30/all-pages"
    # saveImg(readmanganatoParser(url))
    referer = "https://readmanganato.com/"
    referer = ""
    html_class = "container-chapter-reader"
    html_class = "ch-images ch-image-container"
    a = ParsPage(url=url, html_class=html_class, referer=referer)
    a.geturlsimgs()
    a.corecturlsimgs("https://www.readm.org")
    a.geturlsimgs()

    print()
