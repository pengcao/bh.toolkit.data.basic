#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: NumpyCompare.py
@time: 2018/6/2 13:33
@desc: 对三种数据结构（list/array/numpy.array）分别使用三种方法（for/sum/numpy.sum）进行求和
       进行测试，测试这三种方法对于不同的结构的数据进行求解的时候，效率怎么样？
       测试的时候使用的是第三方的库，timeit，主要用到的是timeit.timeit方法
       timeit(stmt='pass', setup='pass', timer=<defaulttimer>, number=1000000)
       返回：
            返回执行stmt这段代码number遍所用的时间，单位为秒，float型
       参数：
            stmt：要执行的那段代码
            setup：执行代码的准备工作，不计入时间，一般是import之类的
            timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管
            number：要执行stmt多少遍
        经过测试发现，numpy.sum对numpy.array进行求和的时候效率最高
'''

import timeit

common_for = """
for d in data:
    s += d
"""

common_sum = """
sum(data)
"""

common_numpy_sum = """
numpy.sum(data)
"""

def timeit_list(n, loops):
    list_setup = """
import numpy
data = [1] * {}
s = 0
""".format(n)
    print('list:')
    print(timeit.timeit(common_for, list_setup, number = loops))
    print(timeit.timeit(common_sum, list_setup, number = loops))
    print(timeit.timeit(common_numpy_sum, list_setup, number = loops))

def timeit_array(n, loops):
    array_setup = """
import numpy
import array
data = array.array('L', [1] * {})
s = 0
""".format(n)
    print('array:')
    print(timeit.timeit(common_for, array_setup, number = loops))
    print(timeit.timeit(common_sum, array_setup, number = loops))
    print(timeit.timeit(common_numpy_sum, array_setup, number = loops))

def timeit_numpy(n, loops):
    numpy_setup = """
import numpy
data = numpy.array([1] * {})
s = 0
""".format(n)
    print('numpy:')
    print(timeit.timeit(common_for, numpy_setup, number = loops))
    print(timeit.timeit(common_sum, numpy_setup, number = loops))
    print(timeit.timeit(common_numpy_sum, numpy_setup, number = loops))

if __name__ == '__main__':
    timeit_list(50000, 500)
    timeit_array(50000, 500)
    timeit_numpy(50000, 500)

