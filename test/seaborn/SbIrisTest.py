#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: SbIrisTest.py
@time: 2018/5/25 8:51
@desc:
'''

import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # load iris dataset
    iris = sns.load_dataset('iris')
    # Construct iris plot
    sns.swarmplot(x='species',y='petal_length',data=iris)
    # show
    plt.show()