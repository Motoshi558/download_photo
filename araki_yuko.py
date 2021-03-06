import requests
from bs4 import BeautifulSoup
import lxml
import urllib.request
import urllib.request
import sys, os

query_word = sys.argv[0]

for num in range(2):
    headers = {"UserAgent": "hoge"}
    URL = "https://search.yahoo.co.jp/image/search?p={0}&ei=UTF-8&b=1={1}".format(query_word, 1 + 20*num)
    resp =requests.get(URL, timeout=1, headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")

    imgs = soup.find_all(alt="「{}」の画像検索結果".format(query_word))

    for i in range(len(imgs)):
        dir_name = "./data/{0}".format(query_word)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        filepath = dir_name + "/{0}-{1}.jpg".format(num, i)
        urllib.request.urlretrieve(imgs[i]["src"], filepath)
