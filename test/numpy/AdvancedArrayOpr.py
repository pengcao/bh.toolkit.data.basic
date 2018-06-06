#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: AdvancedArrayOpr.py
@time: 2018/6/5 23:12
@desc:
'''
import numpy as np
import numpy.random as np_random

if __name__ == '__main__':
    print("将一维数组转换为二维数组")
    arr = np.arange(8)
    print(arr.reshape((4, 2)))
    print(arr.reshape((4, 2)).reshape((2, 4)))  # 支持链式操作

    print("维度大小自动推导")
    arr = np.arange(15)
    print(arr.reshape((5, -1)))

    print("获取维度信息并应用")
    other_arr = np.ones((3, 5))
    print(other_arr)
    print(other_arr.shape)
    print(arr.reshape(other_arr.shape))

    print("高维数组拉平")
    arr = np.arange(15).reshape((5, 3))
    print(arr.ravel())

    print('========================= 高级应用 数组的合并和拆分')
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    print(np.concatenate([arr1, arr2], axis=0))  # 按行连接
    print(np.concatenate([arr1, arr2], axis=1))  # 按列连接

    # 所谓堆叠，参考叠盘子。。。连接的另一种表述
    print('垂直stack与水平stack')
    print(np.vstack((arr1, arr2)))  # 垂直堆叠
    print(np.hstack((arr1, arr2)))  # 水平堆叠
    print

    print('拆分数组')
    arr = np_random.randn(5, 5)
    print(arr)
    print('水平拆分')
    first, second, third = np.split(arr, [1, 3], axis=0)
    print('first')
    print(first)
    print('second')
    print(second)
    print('third')
    print(third)
    print('垂直拆分')
    first, second, third = np.split(arr, [1, 3], axis=1)
    print('first')
    print(first)
    print('second')
    print(second)
    print('third')
    print(third)

    # 堆叠辅助类
    arr = np.arange(6)
    arr1 = arr.reshape((3, 2))
    arr2 = np_random.randn(3, 2)
    print('r_用于按行堆叠')
    print
    np.r_[arr1, arr2]
    print('c_用于按列堆叠')
    print
    np.c_[np.r_[arr1, arr2], arr]
    print('切片直接转为数组')
    print(np.c_[1:6, -10:-5])
    print("================= 高级应用 元素的重复操作")
    print('Repeat: 按元素')
    arr = np.arange(3)
    print(arr.repeat(3))
    print(arr.repeat([2, 3, 4]))  # 3个元素，分别复制2, 3, 4次。长度要匹配！

    print('Repeat，指定轴')
    arr = np_random.randn(2, 2)
    print(arr)
    print(arr.repeat(2, axis=0))  # 按行repeat
    print(arr.repeat(2, axis=1))  # 按列repeat
    print(arr.repeat(2, axis=0))  # 按行repeat

    print('Tile: 参考贴瓷砖')
    print(np.tile(arr, 2))
    print(np.tile(arr, (2, 3)))  # 指定每个轴的tile次数

    print("============== 高级应用 花式索引的等价函数")
    print(')Fancy Indexing例子代码')
    arr = np.arange(10) * 100
    inds = [7, 1, 2, 6]
    print(arr[inds])

    print(')使用take')
    print(arr.take(inds))

    print(')使用put更新内容')
    arr.put(inds, 50)
    print(arr)
    arr.put(inds, [70, 10, 20, 60])
    print(arr)

    print(')take，指定轴')
    arr = np_random.randn(2, 4)
    inds = [2, 0, 2, 1]
    print(arr)
    print(arr.take(inds, axis=1))  # 按列take