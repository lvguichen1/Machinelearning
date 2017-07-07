#!/usr/bin/python
# -*- coding:utf-8 -*-


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    stock_max, stock_min, stock_close, stock_amount = np.loadtxt('SH600000.txt', delimiter='\t', skiprows=2,
                                                                 usecols=(2, 3, 4, 5), unpack=True)
    N = 100
    stock_close = stock_close[:N]
    print stock_close

    n = 10
    # ones 返回填满1的数组
    weight = np.ones(n)
    weight /= weight.sum()
    print weight
    # convolve
    stock_sma = np.convolve(stock_close, weight, mode='valid')  # simple moving average

    weight = np.linspace(1, 0, n)
    weight = np.exp(weight)
    weight /= weight.sum()
    print weight
    stock_ema = np.convolve(stock_close, weight, mode='valid')  # exponential moving average

    t = np.arange(n - 1, N)
    # polyfit 最小二乘多项式拟合
    poly = np.polyfit(t, stock_ema, 10)
    print poly
    # polyval 以特定值评估多项式
    stock_ema_hat = np.polyval(poly, t)
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(facecolor='w')
    plt.plot(np.arange(N), stock_close, 'ro-', linewidth=2, label=u'原始收盘价')
    t = np.arange(n-1, N)
    plt.plot(t, stock_sma, 'b-', linewidth=2, label=u'简单移动平均线')
    plt.plot(t, stock_ema, 'g-', linewidth=2, label=u'指数移动平均线')
    plt.legend(loc='upper right')
    plt.title(u'股票收盘价与滑动平均线MA', fontsize=18)
    plt.grid(True)
    plt.show()
