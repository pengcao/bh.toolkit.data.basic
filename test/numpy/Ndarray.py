#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2017-2020, deamoncao@163.com 
@contact: deamoncao100@gmail.com
@software: garner
@file: Ndarray.py
@time: 2018/6/2 14:36
@desc: 这个是关于numpy array operation test
'''
import numpy as np
import numpy.random as np_random
import matplotlib.pyplot as plt
import pylab

if __name__ == '__main__':
    print("========================使用普通一维数组生成Numpy一维数组")
    data = [6,7.5,8,0,1]
    arr = np.array(data)
    print(arr)
    print("打印元素类型")
    print(arr.dtype)
    print("======================== 使用普通二维数组生成Numpy二维数组")
    data = [[1,2,3,4],[5,6,7,8]]
    arr = np.array(data)
    print(arr)
    print("打印数组维度")
    print(arr.shape)
    print("=== 使用zeros/empty")
    # 生成包含10个0的一维数组
    print(np.zeros(10))
    # 生成3*6的二维数组
    print("生成3*6的二维数组:")
    print(np.zeros((3,6)))
    # 生成2*3*2的三维数组，所有元素未初始化
    print("生成2*3*2的三维数组")
    print(np.empty((2,3,2)))
    print("======================== 使用arrange生成连续元素")
    print(np.arange(15))
    print("=== 对数组进行运算")
    arr = np.array([[1.0,2.0,3.0],[4.,5.,6.]])
    print("*** 对数组进行相乘")
    print(arr * arr)
    print("*** 对数组之间进行相减运算")
    print(arr - arr)
    # 标量操作作用在数组的每个元素上
    arr = np.array([[1.0,2.0,3.0],[4.,5.,6.]])
    print("*** 数组的倒数")
    print(1/arr)
    print("*** 数组进行开根号")
    print(arr ** 0.5)
    # 对数据进行操作  索引和切片
    print("通过索引访问二维数组某一行或某个元素")
    arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(" arr[2] : ",arr[2])
    print(" arr[0][2] : ",arr[0][2])
    # 注意这个功能在普通的Python数组中不能用
    print(" arr[0,2] : ",arr[0,2])
    print("对更高维度数组的访问和操作")
    arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    print(" arr[0] : ",arr[0])
    print(" arr[1,0] : ",arr[1,0])
    # 复制arr[0]的值
    old_value = arr[0].copy()
    # 把arr[0]所有的元素都设置为同一个值
    arr[0] = 42
    print(arr)
    # 把原来的数组写回来
    arr[0] = old_value
    print(arr)

    print("======================== 使用切片访问和操作数组")
    arr = np.array([1,2,3,4,5,6,7,8,9,10])
    print("打印元素arr[1]到arr[5]")
    print(arr[1:6])
    arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("打印第1、2行")
    print(arr[:2])
    print("打印第1、2行，第2、3列")
    print(arr[:2,1:])
    print("打印第一列的所有元素")
    print(arr[:,:1])
    print("第1、2行，第2、3列的元素设置为0")
    arr[:2,1:] = 0
    print(arr)
    print("=========使用布尔数组作为索引")
    name_arr = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
    print("随机生成7*4数组")
    rnd_arr = np_random.randn(7,4)
    print(rnd_arr)
    print("返回布尔数组，元素等于'Bob'为True,否则False")
    print(name_arr == 'Bob')
    print("利用布尔数组选择行")
    print(rnd_arr[name_arr == 'Bob'])
    print("增加限制打印列的范围")
    print(rnd_arr[name_arr == 'Bob',:2])
    print("对布尔数组的内容取反")
    print(rnd_arr[(name_arr == 'Bob')])
    print("逻辑运算混合结果")
    mask_arr = (name_arr == 'Bob') | (name_arr == 'Will')
    print(rnd_arr[mask_arr])
    print("先布尔数组选择行，然后把每行的元素设置为7")
    rnd_arr[name_arr != 'Joe'] = 7
    print(rnd_arr)
    print("======================== Fancy Indexing: 使用整数数组作为索引")
    arr = np.empty((8,4))
    for ii in range(8):
        arr[ii] = ii
    print(arr)
    print("打印arr[4]、arr[3]、arr[0]和arr[6]。")
    print(arr[[4,3,0,6]])
    print("打印arr[3]、arr[5]和arr[-7]行")
    print(arr[[-3,-5,-7]])
    print("通过reshape变换成二维数组")
    arr = np.arange(32).reshape((8,4))
    print("转换之后的数组：",arr)
    print("打印arr[1,0]、arr[5,3]、arr[7,1]和arr[2,2]")
    print(arr[[1,5,7,2],[0,3,1,2]])
    print("1572行的0312列")
    print(arr[[1,5,7,2]][:,[0,3,1,2]])
    print("可读性更好的写法")
    print(arr[np.ix_([1,5,7,2],[0,3,1,2])])
    print("============================== 进行矩阵运算")
    print("*** 转置矩阵")
    arr = np.arange(15).reshape((3,5))
    print(arr)
    print(arr.T)
    print("*** 转置矩阵做点积")
    arr = np_random.randn(6,3)
    print(np.dot(arr.T,arr))
    print("*** 高维矩阵转换")
    arr = np.arange(16).reshape((2,2,4))
    print(arr)
    '''
    详细解释：
    arr数组的内容为
    - a[0][0] = [0, 1, 2, 3]
    - a[0][1] = [4, 5, 6, 7]
    - a[1][0] = [8, 9, 10, 11]
    - a[1][1] = [12, 13, 14, 15]
    transpose的参数为坐标，正常顺序为(0, 1, 2, ... , n - 1)，
    现在传入的为(1, 0, 2)代表a[x][y][z] = a[y][x][z]，第0个和第1个坐标互换。
    - a'[0][0] = a[0][0] = [0, 1, 2, 3]
    - a'[0][1] = a[1][0] = [8, 9, 10, 11]
    - a'[1][0] = a[0][1] = [4, 5, 6, 7]
    - a'[1][1] = a[1][1] = [12, 13, 14, 15]
    '''
    print("*** transpose   ")
    print(arr.transpose((1, 0, 2)))
    print("***直接交换第1和第2个坐标")
    print(arr.swapaxes(1, 2))
    print("=========== 对数组进行函数运算")
    print("*** 求平方根")
    arr = np.arange(10)
    print(np.sqrt(arr))
    print("*** 数组比较")
    x = np_random.randn(8)
    y = np_random.randn(8)
    print(np.maximum(x,y))
    print("*** 使用modf函数把浮点数分解成整数和小数部分")
    arr = np_random.randn(7) * 5 # 统一乘5
    print(np.modf(arr))
    print("==================== 利用数组进行数据处理 简介")
    # 生成100个点
    points = np.arange(-5,5,0.01)
    print('*** points :',points)
    # xs,ys互为转置矩阵
    xs,ys = np.meshgrid(points,points)
    print(" xs : ",xs)
    print(" ys : ",ys)
    z = np.sqrt(xs ** 2 + ys ** 2)
    print("*** sqrt z : ",z)
    # 画图
    plt.imshow(z , cmap = plt.cm.gray)
    plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    pylab.show()