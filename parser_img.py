import requests
from bs4 import BeautifulSoup








Referer = "https://readmanganato.com/"  # запрос для сервера тип с сайта
url1 = "https://mn.mkklcdnv6temp.com/img/tab_3/00/05/23/ax951880/chapter_3745/1-o.jpg" ## ccskrf yf bpj,hf;tybt
# url = "https://readmanganato.com/manga-dg980989/chapter-140"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

s = requests.session()
s.headers.update({'referer': Referer})
img = s.get(url1)

img_file = open('B:/Data/1.jpg', 'wb')
img_file.write(img.content)
img_file.close()


