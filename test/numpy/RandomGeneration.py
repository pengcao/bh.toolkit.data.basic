#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: RandomGeneration.py
@time: 2018/6/5 23:03
@desc:
'''
import numpy as np
import numpy.random as np_random
from random import normalvariate

if __name__ == '__main__':
    print("============== 正态分布随机数")
    samples = np.random.normal(size=(4,4))
    print(samples)
    print("*** 批量按正态分布生成0到1的随机数")
    N = 10
    print([normalvariate(0,1) for _ in range(N)])
    print("*** 与上面代码等价")
    print(np.random.normal(size=N))