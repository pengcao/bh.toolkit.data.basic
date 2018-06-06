#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: PythonBasic.py
@time: 2018/5/30 22:01
@desc:
'''

import numpy as np
from scipy import linalg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from igraph import *
# from __future__ import division


if __name__ == '__main__':
    print('============================== numpy test ')
    list = np.arange(10)
    print('list type : ',type(list),' ; value : ',list)
    print(list**2)
    print('============================== scipy test')
    A = np.array([[1,2],[3,4]])
    print(A)
    # 矩阵求行列式（标量）
    print('矩阵求行列式：',linalg.det(A))
    # 矩阵求逆
    print('矩阵求逆：',linalg.inv(A))
    print('============================== pandas test ')
    s = pd.Series([1,3,5,np.nan,6,8])
    print('pandas series : ',s)
    dateArray = pd.date_range('20130101', periods=6)
    print('date_range : ',dateArray)
    valueArray = np.random.randn(6,4)
    # df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    columnList = ['A', 'B', 'C', 'D']
    # columnList = list('ABCD')
    df = pd.DataFrame(valueArray, index=dateArray, columns=columnList)
    print('pandas dataframe: ',df)
    print(' head : ',df.head())
    print(' tail :',df.tail())
    print(' describe : ' , df.describe())
    print(' T : ',df.T)
    print(' sort :',df.sort_values(by = 'B'))

    print('============================== plot test')
    plt.plot([1,2,3])
    plt.ylabel('some numbers')
    plt.show()
    print('============================== seaborn test')
    sns.set(color_codes=True)
    x = np.random.normal(size=100)
    sns.distplot(x)
    plt.show()
    print('============================== nltk test')
    print('============================== igraph test')
    g = Graph([(0, 1), (0, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)])
    print(g)
    print('=== igraph summary : ',summary(g))
    print('=== igraph degree : ',g.degree())

    array, target = list(np.arange(2, 32046, 2)), 16021




