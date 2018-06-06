#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: ThreatBook.py
@time: 2018/5/31 10:15
@desc:
'''

import http.client, mimetypes
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import os
import sys
import optparse
import hashlib
import time

# The apikey.
API_KEY = "0327e9fcbc0e43f59e934973acb77788b75e16616275459fbac2b3e97d343d2e"

class ThreatBook(object):
    def __init__(self, api_key):
        super(ThreatBook, self).__init__()
        self.api_key = api_key

    def __repr__(self):
        return "<ThreatBook proxy>"

    def get(self, domain):
        print("Getting the result ...\r\n")

        url = "https://x.threatbook.cn/api/v1/domain/query"
        # url = "http://localhost:9000/api/v1/domain/query"
        parameters = {"domain": domain, "apikey": self.api_key, "field": "cur_ips"}
        data = urllib.parse.urlencode(parameters)
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        ret_json = response.read()
        print("Report(in JSON):\r\n")
        print(ret_json)
        return 1;

if __name__ == "__main__":
    dm = 'https://120.92.86.100'
    threatBook = ThreatBook(API_KEY)
    threatBook.get(dm)