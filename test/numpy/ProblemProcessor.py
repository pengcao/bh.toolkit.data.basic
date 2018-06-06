#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: ProblemProcessor.py
@time: 2018/6/5 23:38
@desc: 矩阵运算  求矩阵之间的距离
'''
import numpy as np
import numpy.linalg as la
import time

if __name__ == '__main__':
    X = np.array([range(0, 500), range(500, 1000)])
    m, n = X.shape

    t = time.time()
    print("=== start time : ",t)
    D = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1, n):
            D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
            # print("两个向量相减 ： ",la.norm(X[:, i] - X[:, j]))
            D[j, i] = D[i, j]
    print(time.time() - t)

    t = time.time()
    D = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1, n):
            d = X[:, i] - X[:, j]
            D[i, j] = np.dot(d, d)
            D[j, i] = D[i, j]
    print(time.time() - t)

    t = time.time()
    G = np.dot(X.T, X)
    D = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1, n):
            D[i, j] = G[i, i] - G[i, j] * 2 + G[j, j]
            D[j, i] = D[i, j]
    print(time.time() - t)

    t = time.time()
    G = np.dot(X.T, X)
    H = np.tile(np.diag(G), (n, 1))
    D = H + H.T - G * 2
    print(time.time() - t)
