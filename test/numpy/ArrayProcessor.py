#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: ArrayProcessor.py
@time: 2018/6/4 22:21
@desc:
'''

import numpy as np
import numpy.random as np_random

'''
关于zip函数的一点解释，zip可以接受任意多参数，然后重新组合成1个tuple列表。
zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
返回结果：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''

if __name__ == '__main__':
    print("============ 利用数组进行数据处理 将条件逻辑表述为数组运算")
    print("======== 通过真值表选择元素")
    x_arr = np.array([1.1,1.2,1.3,1.4,1.5])
    y_arr = np.array([2.1,2.2,2.3,2.4,2.5])
    cond = np.array([True,False,True,True,False])
    # 通过列表推导实现
    result = [(x if c else y) for x,y,c in zip(x_arr,y_arr,cond)]
    print(" result : ",result)
    print("使用Numpy的where函数")
    print(np.where(cond,x_arr,y_arr))
    print("============ 利用数组进行数据处理 数学和统计方法")
    print("*** 求和、求平均")
    arr = np.random.randn(5,4)
    print(arr)
    print(arr.mean())
    print(arr.sum())
    print("*** 对每一行的元素求平均")
    print(arr.mean(axis=1))
    print("*** 对每一列元素求和，axis可以省略")
    '''
    cumsum:
    - 按列操作：a[i][j] += a[i - 1][j]
    - 按行操作：a[i][j] *= a[i][j - 1]
    cumprod:
    - 按列操作：a[i][j] += a[i - 1][j]
    - 按行操作：a[i][j] *= a[i][j - 1]
    '''
    print("*** cunsum和cumprond函数演示")
    arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
    print(arr.cumsum(0))
    print(arr.cumprod(1))
    print("====================== 利用数组进行数据处理 用于布尔型数组的方法")
    print("*** 对正数求和")
    arr = np_random.randn(100)
    print((arr > 0).sum())
    print("*** 对数组逻辑操作")
    bools = np.array([False,False,True,False])
    print("*** 有一个为True则返回True")
    print(bools.any())
    print("*** 有一个为False则返回False")
    print(bools.all())
    print("====================== 利用数组进行数据处理 排序")
    print("*** 一维数组排序")
    arr = np_random.randn(8)
    arr.sort()
    print(arr)
    print("*** 二维数组排序")
    arr = np_random.randn(5,3)
    print(arr)
    print("*** 对每一行元素做排序")
    arr.sort(1)
    print(arr)
    print("*** 找位置在5%的数字")
    large_arr = np_random.randn(1000)
    large_arr.sort()
    print(large_arr[int(0.05*len(large_arr))])
    print("====================== 利用数组进行数据处理 去重以及其它集合运算")
    print("*** 用unique函数去重")
    names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
    print("*** 传统Python做法")
    print(np.unique(names))
    ints = np.array([3,3,3,2,2,1,1,4,4])
    print(np.unique(ints))
    print("*** 查找数组元素是否在另一数组")
    values = np.array([6,0,0,3,2,5,6])
    print(np.in1d(values,[2,3,6]))
