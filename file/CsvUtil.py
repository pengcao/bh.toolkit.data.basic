#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: CsvUtil.py
@time: 2018/5/21 12:24
@desc:
'''

import csv
from log.Logger import Logger
import sys

class CsvUtil(object):
    __logger = Logger(sys.modules['__main__'])

    def readCsvRntnList(self,filePath):
        '''
        读取csv文件的内容并且返回
        :param filePath:
        :param fileName:
        :return:
        '''
        # return list
        rntnList = []
        # 以rb的方式打开csv文件
        file = open(filePath,'r',encoding="utf-8")
        reader = csv.reader(file)
        for line in reader:
            rntnList.append(line)
        file.close()
        return rntnList

    def readCsvRntnDictList(self,filePath):
        '''
        读取csv并且返回List[dict,dict,...,dict]
        :param filePath:
        :return:
        '''
        #
        rntnDictList = []
        #
        file  = open(filePath,'r',encoding="utf-8")
        reader = csv.reader(file)
        # csv line : reader.line_num
        headRow = next(reader)
        totalColumns = len(headRow)
        for row in reader:
            dict = {}
            for ii in range(totalColumns):
                dict[headRow[ii]] = row[ii]
            rntnDictList.append(dict)
        return rntnDictList

    def writeContent2Csv(self,filePath,valueList):
        '''
        往csv文件中写内容
        :param filePath:
        :param valueList:
        :return:
        '''
        file = open(filePath,'w',newline='')
        writer = csv.writer(file)
        #
        writer.writerows(valueList)
        file.close()

    def writeList2Csv(self,filePath,valueList,headList):
        '''
        往csv文件中写内容
        :param filePath:
        :param valueList:
        :param headList:
        :return:
        '''
        file = open(filePath,'w',newline='')
        writer = csv.writer(file)
        #
        writer.writerow(headList)
        writer.writerows(valueList)
        file.close()

    def writeDictList2Csv(self,filePath,dictList,headList):
        '''
        往csv文件中写内容
        :param filePath:
        :param dictList:
        :param headList:
        :return:
        '''
        file = open(filePath,'w',newline='')
        writer = csv.writer(file)
        #
        writer.writerow(headList)
        totalColumns = len(headList)
        for dict in dictList:
            row = []
            for ii in range(totalColumns):
                row.append(dict[headList[ii]])
            writer.writerow(row)
        file.close()



if __name__ == '__main__':
    csvUtil = CsvUtil()
    csvFilePath = 'C:/develop/csv_test_0003.csv'
    headList = ['id','name','age']
    # read
    print(csvUtil.readCsvRntnList(csvFilePath))
    print(csvUtil.readCsvRntnDictList(csvFilePath))
    # write
    # valueList = [[1,'aaa',25],[2,'bbb',26],[3,'ccc',27]]
    # #
    #
    # csvUtil.writeList2Csv(csvFilePath,valueList,headList)


