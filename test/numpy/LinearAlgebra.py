#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: LinearAlgebra.py
@time: 2018/6/5 22:45
@desc:
'''
import numpy as np
import numpy.random as np_random
from numpy.linalg import inv,qr

if __name__ == '__main__':
    print("=========== 矩阵乘法")
    x = np.array([[1.,2.,3.],[4.,5.,6.]])
    y = np.array([[6.,23.],[-1,7],[8,9]])
    print("矩阵乘法x.dot(y)：",x.dot(y))
    print(" np.ones(3)  : ",np.ones(3))
    print(" np.dot(x,np.ones(3)) : ",np.dot(x,np.ones(3)))
    x = np_random.randn(5,5)
    print("============ 矩阵求逆")
    mat = x.T.dot(x)
    print(" 矩阵求逆inv(mat) ： ",inv(mat))
    print("*** 与逆矩阵相乘，得到单位矩阵")
    print(mat.dot(inv(mat)))
    print("***   矩阵消元")
    print(mat)
    q,r = qr(mat)
    print("q :",q)
    print("r :",r)
    # TODO: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.qr.html q代表什么矩阵？
