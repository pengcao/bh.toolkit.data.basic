#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: FileUtil.py
@time: 2018/5/17 23:36
@desc: This is a module to oprate files
'''

import os,sys
import codecs
from log.Logger import Logger

class FileUtil(object):
    """
        create a private variable __logger to log infomation
    """
    __logger = Logger(sys.modules['__main__'])

    def getFileListByExtension(self,dirPath,extension):
        """
        @summary:
        @param dirPath：This is Directory Path
        @param extension: This is file extension name
        """
        extensionFileList = []
        extensionName = '.'+extension #
        # get directory files
        fileList = os.listdir(dirPath)
        for file in fileList:
            # judge the files of directory,if file extension is equal the giving extension,then  to return
            if os.path.splitext(file)[1] == extensionName:
                extensionFileList.append(file)
        return extensionFileList

    def writeToFile(self,filePath,content):
        """
        @sumary: write the content to the file
        @param filePath: the file to writing contents and the encoding is utf8
        @param content: the contents
        """
        # file oprate model is appending and writing, the encoding is utf8
        fileWrObj = codecs.open(filePath,'a',encoding='utf8')
        fileWrObj.write(content)
        fileWrObj.close()

    def readFromFile(self, filePath):
        """
        @sumary:read file content
        @param filePath: the file path is to read
        @param content: the content of file
        """
        content = None
        try:
            # just read the content of file using the encoding utf8
            fileReadObj = codecs.open(filePath, 'r', encoding='utf8')
            content = fileReadObj.read()
            fileReadObj.close()
        except Exception as e:
            errMsg = 'read file '+filePath+' failure'
            self.__logger.error(errMsg)
        return content

    def getFilePath(self,fileName):
        """
        @summary:file path,os.path.dirname(sys.path[0])+'/conf/teste.txt'
        @param fileName:
        """
        filePath  = os.path.dirname(sys.path[0])+fileName
        return filePath

if __name__ == '__main__':
    print('FileUtil.py')
    mod = sys.modules['__main__']
    file = getattr(mod, '__file__', None)
    print("mod : " , mod)
    print("file : ", file)
    print(os.path.splitext(os.path.basename(file))[0])
    # filename = '/conf/address.json'
    filename = '/conf/districtDict.txt'
    print("path : " + os.path.splitext(file)[1])
    fileUtil = FileUtil()
    fullfilename = fileUtil.getFilePath(filename)
    content = fileUtil.readFromFile(fullfilename)
    print(content)