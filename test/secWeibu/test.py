#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com
@contact: deamoncao100@gmail.com
@software: garner
@file: test.py
@time: 2018/5/31 10:23
@desc:
'''

import httplib, mimetypes
import urllib
import urllib2
import os
import sys
import optparse
import hashlib
import time

# The apikey.
API_KEY = "PUT YOUR APIKEY HERE"


class ThreatBook(object):
    def __init__(self, api_key):
        super(ThreatBook, self).__init__()
        self.api_key = api_key

    def __repr__(self):
        return "<ThreatBook proxy>"

    def get(self, domain):
        print
        "Getting the result ...\r\n"

        url = "https://x.threatbook.cn/api/v1/domain/query"
        # url = "http://localhost:9000/api/v1/domain/query"
        parameters = {"domain": domain, "apikey": self.api_key, "field": "cur_ips"}
        data = urllib.urlencode(parameters)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        ret_json = response.read()
        print("Report(in JSON):\r\n")
        print(ret_json)
        return 1;


def main():
    parser = optparse.OptionParser(usage="""
    %prog <domain>
Samples:
    %prog manage-163-account.com
    """)

    (options, arguments) = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        return -1

    domain = arguments.pop(0)

    try:
        v = ThreatBook(API_KEY)
        v.get(domain)

    except Exception as e:
        print("ThreatBook returned a non correct response. See the parameter -l")


if __name__ == "__main__":
    main()