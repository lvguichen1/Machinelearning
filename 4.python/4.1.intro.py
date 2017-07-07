#!/usr/bin/python
# -*- coding:utf-8 -*-

# 导入NumPy函数库，一般都是用这样的形式(包括别名np，几乎是约定俗成的)
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
from scipy import stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import scipy as sp
import math
import seaborn


def residual(t, x, y):
    return y - (t[0] * x ** 2 + t[1] * x + t[2])


def residual2(t, x, y):
    print t[0], t[1]
    return y - (t[0] * np.sin(t[1] * x) + t[2])


# x ** x          x > 0
# (-x) ** (-x)    x < 0
def f(x):
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[i])
    return y


if __name__ == "__main__":
    # numpy是非常好用的数据包，如：可以这样得到这个二维数组
    # [[ 0  1  2  3  4  5]
    #  [10 11 12 13 14 15]
    #  [20 21 22 23 24 25]
    #  [30 31 32 33 34 35]
    #  [40 41 42 43 44 45]
    #  [50 51 52 53 54 55]]
    # a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(6)
    # print a

    # 标准Python的列表(list)中，元素本质是对象。
    # 如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。
    # 因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。

    # # 1.使用array创建
    # 通过array函数传递list对象
    # L = [1, 2, 3, 4, 5, 6]
    # print "L = ", L
    # a = np.array(L)
    # print "a = ", a
    # print type(a), type(L)
    # 若传递的是多层嵌套的list,将创建多维数组
    # b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # print b

    # 数组大小可以通过其shape属性获得
    # print a.shape
    # print b.shape

    # 强制修改shape
    # b.shape = 4, 3
    # print b
    # 注：从(3,4)改为(4,3)并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变
    # c = b.reshape((3, -1))
    # print "b = \n", b
    # print 'c = \n', c

    # 数组b和c共享内存，修改任意一个将影响另外一个
    # b[1][1] = 20
    # print "b = \n", b
    # print "c = \n", c

    # 数组的元素类型可以通过dtype属性获得
    # print a.dtype
    # print b.dtype

    # 可以通过dtype参数在创建时指定元素类型
    # d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float)
    # f = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.complex)
    # print d
    # print f

    # 如果更改元素类型，可以使用astype安全的转换
    # f = d.astype(np.int)
    # print f

    # 但不要强制仅修改元素类型，如下面这句，将会以int来解释单精度float类型
    # d.dtype = np.int
    # print d

    # 2.使用函数创建
    # 如果生成一定规则的数据，可以使用NumPy提供的专门函数
    # arange函数类似于python的range函数：指定起始值、终止值和步长来创建数组
    # 和Python的range类似，arange同样不包括终值；但arange可以生成浮点类型，而range只能是整数类型
    # np.set_printoptions(linewidth=100, suppress=True)
    # a = np.arange(1, 10, 0.5)
    # print a

    # linspace函数通过指定起始值、终止值和元素个数来创建数组，缺省包括终止值
    # b = np.linspace(1, 10, 10)
    # print 'b = ', b

    # 可以通过endpoint关键字指定是否包括终值
    # c = np.linspace(1, 10, 10, endpoint=False)
    # print 'c = ', c

    # 和linspace类似，logspace可以创建等比数列
    # 下面函数创建起始值为10^1，终止值为10^2，有10个数的等比数列
    # d = np.logspace(1, 4, 4, endpoint=True, base=2)
    # print d

    # 下面创建起始值为2^0，终止值为2^10(包括)，有10个数的等比数列
    # f = np.logspace(0, 10, 11, endpoint=True, base=2)
    # print f

    # 使用 frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
    # s = 'abcdzzzz'
    # g = np.fromstring(s, dtype = np.int8)
    # print g

    # 3.存取
    # 3.1常规办法：数组元素的存取方法和Python的标准方法相同
    # a = np.arange(10)
    # print a
    # # 获取某个元素
    # print a[3]
    # # 切片[3,6)，左闭右开
    # print a[3:6]
    # # 省略开始下标，表示从0开始
    # print a[:5]
    # # 下标为负标识从后向前数
    # print a[:-3]
    # # 步长为2
    # print a[1:9:2]
    # # 步长为-1，即翻转
    # print a [::-1]
    # # 切片数据是原数组的一个视图，与原数组共享内容空间，可以直接修改元素值
    # a[1:4] = 10, 20, 30
    # # 因此，在实践中，切实注意原始数据是否被破坏，如：
    # b = a[2:5]
    # b[0] = 200
    # print a

    # 3.2 整数/布尔数组存取
    # 3.2.1
    # 根据整数数组存取：当使用整数序列对数组元素进行存取时，
    # 将使用整数序列中的每个元素作为下标，整数序列可以是列表(list)或者数组(ndarray)。
    # 使用整数序列作为下标获得的数组不和原始数组共享数据空间。
    # a = np.logspace(0, 9, 10, base=2)
    # print a
    # i = np.arange(0, 10, 2)
    # print i
    # # 利用i取a中的元素
    # b = a[i]
    # print b
    # # b的元素更改，a中元素不受影响
    # b[2] = 1.6
    # print b
    # print a

    # 3.2.2
    # 使用布尔数组i作为下标存取数组a中的元素：返回数组a中所有在数组b中对应下标为True的元素
    # 生成10个满足[0,1)中均匀分布的随机数
    # a = np.random.rand(10)
    # print a
    # 大于0.5的元素索引
    # print a > 0.5
    # 大于0.5的元素
    # b = a[a > 0.5]
    # print b
    # 将原数组中大于0.5的元素截取成0.5
    # a[a > 0.5] = 0.5
    # print a
    # b不受影响
    # print b

    # 3.3 二维数组的切片
    # [[ 0  1  2  3  4  5]
    #  [10 11 12 13 14 15]
    #  [20 21 22 23 24 25]
    #  [30 31 32 33 34 35]
    #  [40 41 42 43 44 45]
    #  [50 51 52 53 54 55]]
    # a = np.arange(0, 60, 10)
    # print 'a = ', a
    # b = a.reshape((-1, 1))
    # print b
    # c = np.arange(6)
    # print c
    # 合并上述代码
    # a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    # print a
    # 二维数组的切片
    # print a[[0, 1, 2], [2, 3, 4]]
    # print a[4, [2, 3, 4]]
    # print a[4:, [2, 3, 4]]
    # i = np.array([True, False, True, False,False, True])
    # print a[i]
    # print a[i, 3]

    # 4.1 numpy与Python数学库的时间比较
    # for j in np.logspace(0, 7, 8):
    #     x = np.linspace(0, 10, j)
    #     start = time.clock()
    #     y = np.sin(x)
    #     t1 = time.clock() - start
    #     x = x.tolist()
    #     start = time.clock()
    #     for i, t in enumerate(x):
    #         x[i] = math.sin(t)
    #     t2 = time.clock() - start
    #     print j, ": ", t1, t2, t2 / t1

    # 4.2 元素去重
    # # 4.2.1 直接使用库函数
    # a = np.array((1, 2, 3, 4, 5, 5, 7, 3, 2, 2, 8, 8))
    # print '原始数组：', a
    # # 使用库函数unique
    # b = np.unique(a)
    # print '去重后：', b
    # 4.2.2 二维数组的去重
    c = np.array(((1, 2), (3, 4), (5, 6), (1, 3), (3, 4), (7, 6)))
    print '二维数组：\n', c
    # print '去重后：', np.unique(c)
    # 4.2.3 方案1：转换为虚数
    # r, i = np.split(c, (1,), axis=1)
    # x = r + i * 1j
    x = c[:0] + c[:1] * 1j
    print '转换成虚数：', x
    print '虚数去重后：', np.unique(x)
    print np.unique(x, return_index=True)
    idx = np.unique(x, return_index=True)[1]
    print '二维数组去重: \n', c[idx]
    # 4.2.3 方案2：利用set
    print '去重方案2: \n', np.array(list(set([tuple(t) for t in c])))
