#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: WeiBuClawer.py
@time: 2018/6/1 14:54
@desc:
'''

import sys,os
import requests
from bs4 import BeautifulSoup
from log.Logger import Logger

class WeiBuClawer(object):
    '''
        claw the site: https://x.threatbook.cn
    '''

    __logger = Logger(sys.modules['__main__'])

    def clawDomain(self,domain):
        '''
        通过域名来爬取威胁情报信息
        :param domain:
        :return:
        '''
        self.__logger.info('claw the site '+domain)
        cdomain = "https://x.threatbook.cn/domain/" + domain
        response = requests.get(cdomain)
        soup = BeautifulSoup(response.text)
        return soup

    def clawIp(self,ip):
        '''
        通过IP来爬取威胁情报信息
        :param ip:
        :return:
        '''
        self.__logger.info('claw the ip : '+ip)
        cIp = "https://x.threatbook.cn/ip/" + ip
        response = requests.get(cIp)
        soup = BeautifulSoup(response.text)
        return soup

    def parseIpGeroInfo(self,soup):
        '''
        解析得到IP的地理位置信息
        :param soup:
        :return:
        '''
        self.__logger.info('parse the html to get ip gero info')
        geroInfo = ''
        infoTab = soup.find("table", "table table-condensed table-borderless pull-left res-brief")
        trList = infoTab.find_all('tr')
        trSize = len(trList)
        if trSize > 2:
            geroTrObj = trList[1]
            geroInfo = geroTrObj.find('td').string.strip()
            if geroInfo is not  None:
                geroInfo = ''.join(geroInfo.split())
        return geroInfo

    def parseWeibuThread(self,soup):
        '''
        解析微步情报
        :param soup:
        :return:
        '''
        self.__logger.info('parse the html to get weibu thread')
        threadStrs = ""
        # threadTab = soup.find(id="tag_td")
        # spanTabList = threadTab.find_all("span","tag non-clickable-tag")
        spanTabList = soup.find_all("span", "tag non-clickable-tag")
        slistSize = len(spanTabList)
        limitSize = slistSize - 1
        for ii in range(slistSize):
            threadStrs = threadStrs + spanTabList[ii].string
            if ii < limitSize:
                threadStrs = threadStrs + ","
        return threadStrs

    def parseComunityThread(self,soup):
        '''
        解析社区情报
        :param soup:
        :return:
        '''
        self.__logger.info('parse the html to get comunity thread')
        threadStrs = ""
        voteList = soup.find_all("span", "vb4-tag voted")
        slistSize = len(voteList)
        limitSize = slistSize - 1
        for ii in range(slistSize):
            threadStrs = threadStrs + voteList[ii].string
            if ii < limitSize:
                threadStrs = threadStrs + ","
        return threadStrs

    def parseThreads(self,soup):
        '''
        解析威胁情报
        :param soup:
        :return:
        '''
        self.__logger.info('parse the html to get threads')
        threadStrs = ""
        threads = soup.find(id="intelli_table")
        threadList = threads.find_all('td')
        listSize = len(threadList)
        limitSize = listSize - 1
        for ii in range(listSize):
            if (ii + 1) % 3 == 0:
                if threadList[ii].string is None:
                    continue
                else:
                    threadStrs = threadStrs + threadList[ii].string
                if ii < limitSize:
                    threadStrs = threadStrs + ","
        return threadStrs

if __name__ == '__main__':
    weiBuClawer = WeiBuClawer()
    # claw ip test
    soup = weiBuClawer.clawIp('120.92.86.100')
    print(' === community thread : ',weiBuClawer.parseComunityThread(soup))
    print(' === Wei Bu    thread : ',weiBuClawer.parseWeibuThread(soup))
    print(' ===           thread : ',weiBuClawer.parseThreads(soup))
    print(' === ip         gero  : ',weiBuClawer.parseIpGeroInfo(soup))
    # claw domain test
    # soup = weiBuClawer.clawDomain("rer.njaavfxcgk3.club")
    # print(' === community thread : ',weiBuClawer.parseComunityThread(soup))
    # print(' === Wei Bu    thread : ',weiBuClawer.parseWeibuThread(soup))
    # print(' ===           thread : ',weiBuClawer.parseThreads(soup))




