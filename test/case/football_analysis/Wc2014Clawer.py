#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: Wc2014Clawer.py
@time: 2018/6/4 8:51
@desc:
      mechanize:用于模拟浏览器登录
      其中mechanize只能用于python2.7不能使用与python3.x.在python3.x中相对应的包有：robobrowser，MechanicalSoup
'''

import requests
import json
import mechanicalsoup
from bs4 import BeautifulSoup
import time

#initializes the browser
# br = mechanize.Browser()
# br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=10)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features':'lxml'
                 }
)



