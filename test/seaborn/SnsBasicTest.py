#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: SnsBasicTest.py
@time: 2018/5/23 22:03
@desc:
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def linePlot():
    #
    sns.set_style("whitegrid")
    print(np.arange(10))
    plt.plot(np.arange(10))
    plt.show()

def snsData():
    dataDir = 'C:/develop/seaborn-data-master/'

    df_iris = pd.read_csv(dataDir + 'iris.csv')
    fig, axes = plt.subplots(1, 2)
    sns.distplot(df_iris['petal_length'], ax=axes[0], kde=True, rug=True)  # kde 密度曲线  rug 边际毛毯
    sns.kdeplot(df_iris['petal length'], ax=axes[1], shade=True)  # shade  阴影
    plt.show()

def boxPlot():
    sns.set(style="ticks")

    # Load the example tips dataset
    tips = sns.load_dataset("tips")

    # Draw a nested boxplot to show bills by day and sex
    sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="PRGn")
    sns.despine(offset=10, trim=True)

#===========================================================================
# 我们将载入seaborn,但是因为载入时会有警告出现，因此先载入warnings，忽略警告
import warnings

warnings.filterwarnings("ignore")

sns.set(style="white", color_codes=True)

# 载入数据
iris = pd.read_csv("C:/develop/data_common/Iris.csv")  # 数据现在为 DataFrame格式
print(type(iris))
# 用head函数看一下数据结构啥样
print(iris.head())
print(iris["Species"].value_counts())
# 使用 .plot 做散点图
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")  # 数据为萼片的长和宽 结果如下
plt.show()
# 开始使用seaborn了它能同时显示直方图
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
plt.show()
# 我们还可以用seaborn's FacetGrid 标记不同的种类
# hue英文是色彩的意思                            # 注意这里的plt哦
sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
plt.show()
#  Seaborn中的boxplot，可以画箱线图，可以看出不同种类的分布情况
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
plt.show()
# 利用striplot可以锦上添花，加上散点图
#
# 使振动值jitter=True 使各个散点分开，要不然会是一条直线
#
# 注意这里将坐标图用ax来保存了哦，这样第二次才会在原来的基础上加点
ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
plt.show()
ax = sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")
plt.show()
# 这图可以变现出密度的分布
sns.violinplot(x="Species", y="PetalLengthCm", data=iris, size=6)
plt.show()
# 通过这个曲线图可以看出不同特征值时的分布密度
sns.FacetGrid(iris, hue="Species", size=6).map(sns.kdeplot, "PetalLengthCm").add_legend()
plt.show()
#  pairplot显示不同特征之间的关系
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)
plt.show()
# 修改参数dige_kind
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")
plt.show()
# 用Pandas 快速做出每个特征在不同种类下的箱线图
iris.drop("Id", axis=1).boxplot(by="Species", figsize=(12, 6))
plt.show()
# # 画图的函数在下面，我们会发现相同种类的线总是缠绵在一起，可以和聚类混在一起噢，事实上他们与欧氏距离是有关系的
# from pandas.tools.plotting import andrews_curves
#
# andrews_curves(iris.drop("Id", axis=1), "Species")


