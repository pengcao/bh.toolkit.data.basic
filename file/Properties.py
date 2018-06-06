#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: Properties.py
@time: 2018/5/19 17:14
@desc: This is the module to read properties file
'''

import sys,os
from log.Logger import Logger

class Properties(object):
    """
        private variable
    """
    __logger = Logger(sys.modules['__main__'])

    def __init__(self,fileName):
        path = sys.path[0]
        self.filePath = os.path.dirname(path) + fileName
        self.properties = {} # 关于配置信息的字典对象
        self.properties = self.initProperties()


    def initProperties(self):
        '''
        初始化配置文件，将配置文件转换成字典对象并且返回
        :return:  字典结构的配置文件
        '''
        try:
            pro_file = open(self.filePath,"Ur")
            for line in pro_file.readlines():
                line = line.strip().replace('\n','')
                if line.find("#")!= -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0])+1:]
                    self.properties[strs[0].strip()] = strs[1].strip()
            try:
                pro_file.close()
            except Exception as ex:
                self.__logger.error("关闭配置文件时，出现错误")
        except Exception as ex:
            raise self.__logger.error("读取配置文件时，出现错误")
        return self.properties

    def getValStrByKey(self,key):
        '''
        根据key获取配置文件中的value
        :param key:
        :return:
        '''
        if self.properties.__contains__(key):
            return self.properties[key]
        else:
            return None

if __name__ == '__main__':
    print()
    dict = {"h1":1,"h2":2}
    print(dict.__contains__("h1"))
    filename = '/conf/email.properties'
    properties = Properties(filename)
    print("sender : ",properties.getValStrByKey("sender"))

