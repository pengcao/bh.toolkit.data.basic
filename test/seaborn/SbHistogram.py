#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: SbHistogram.py
@time: 2018/5/21 12:32
@desc:
'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

if __name__ == '__main__':
    tips = sns.load_dataset("tips")
    g = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
    bins = np.linspace(0, 60, 13)
    g.map(plt.hist, "total_bill", color="steelblue", bins=bins, lw=0)

