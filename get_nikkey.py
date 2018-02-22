# -*- coding: utf-8 -*-

"""
https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406 を参考に、python3系に書き換えて作った。
"""
import requests
from bs4 import BeautifulSoup
target_url = 'http://www.nikkei.com/"'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml')
title_tag = soup.title
title = title_tag.string
print(title_tag)
print(title)
