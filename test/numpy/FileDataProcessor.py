#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: FileDataProcessor.py
@time: 2018/6/5 22:28
@desc:
'''

import numpy as np

if __name__ == '__main__':
    print("=========== 读取csv文件做为数组")
    arr = np.loadtxt('array_ex.txt',delimiter=',')
    print(arr)
    print("============ 数组文件读写")
    arr = np.arange(10)
    np.save('some_array',arr)
    print(np.load('some_array.npy'))
    print("============= 多个数组压缩存储")
    np.savez('array_archive.npz',a = arr, b = arr)
    arch = np.load('array_archive.npz')
    print(arr)
    print(arch['b'])