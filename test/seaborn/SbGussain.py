#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: SbGussain.py
@time: 2018/5/23 8:37
@desc:
'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    sns.set( palette="muted", color_codes=True)
    rs = np.random.RandomState(10)
    d = rs.normal(size=100)
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
    sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
    sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
    sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
    sns.distplot(d, color="m", ax=axes[1, 1])
    plt.show()