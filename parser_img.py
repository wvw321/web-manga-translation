import requests
from bs4 import BeautifulSoup


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
    saveImg(readmanganatoParser(url))

    print()
