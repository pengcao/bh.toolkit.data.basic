#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: clawer_test.py
@time: 2018/6/1 13:50
@desc:
'''

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get("https://x.threatbook.cn/ip/80.82.78.50")
    soup = BeautifulSoup(response.text)
    # print(soup.title.text)
    print(soup)

