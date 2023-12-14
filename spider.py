import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlsplit
import os
import time
head = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}


def is_direct_link(link):
    parsed_link = urlparse(link)
    return bool(parsed_link.netloc)


def download_image(url):
    global success, fail
    response = requests.get(url)
    if response.ok:
        content_type = response.headers.get('content-type')
        if content_type and 'image' in content_type:
            filename = os.path.basename(url)
            # ext = os.path.splitext(url)[1]
            with open(f'{filename}', 'wb') as f:
                f.write(response.content)
                success += 1
            print(f'{filename} dowloaded')
    else:
        filename = os.path.basename(url)
        print(f'Dowload{filename} fail，status code:{response.status_code}')
        fail += 1


def download_file(url):
    response = requests.get(url, headers=head)
    if response.ok:
        domain = "{0.scheme}://{0.netloc}".format(urlsplit(url))
        soup = BeautifulSoup(response.text, "html.parser")
        imgs = soup.find_all("img")
        global success, fail
        success = 0
        fail = 0
        print('--------Creat dirctory---------')
        if os.path.isdir('images'):
            pass
        else:
            os.makedirs('images')
        os.chdir('images')
        if os.path.isdir(f'{url.split("/")[2]}'):
            pass
        else:
            os.mkdir(f'{url.split("/")[2]}')
        os.chdir(f'{url.split("/")[2]}')
        print('--------Dowload images--------')
        for a in imgs:
            time.sleep(0.1)
            src = a.get('src')
            src = src.strip()
            if is_direct_link(src):
                download_image(src)
            else:
                src = domain + '/' + src
                download_image(src)
        os.chdir('../')
        os.chdir('../')
        print('-------Opration finished------')
        print(f'Dowload{success + fail} imgaes.')
        print(f'{success} successed {fail} failed')
        print(f'Dowload time:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')

    else:
        print("请求失败")
        print("请检查网址是否正确或网站状态是否正常")
