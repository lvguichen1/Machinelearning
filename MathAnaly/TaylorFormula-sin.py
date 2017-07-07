#!/usr/bin/python
# -*- coding:utf-8 -*-


import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def calc_sin_small(x):
    x2 = -x ** 2
    t = x
    f = 1
    sum = 0
    for i in range(10):
        sum += t / f
        t *= x2
        f *= ((2 * i + 2) * (2 * i + 3))
    return sum


def calc_sin(x):
    a = x / (2 * np.pi)
    k = np.floor(a)
    a = x - k * 2 * np.pi
    return calc_sin_small(a)


if __name__ == "__main__":
    t = np.linspace(-2 * np.pi, 2 * np.pi)
    print t
    y = np.empty_like(t)
    for i, x in enumerate(t):
        y[i] = calc_sin(x)
        print '\nsin(', x, ')=', y[i], '(近似值)\t', math.sin(x),
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(t, y, 'r-', t, y, 'go', linewidth=2)
    plt.title(u'Taylor展开的应用-sin(x)', fontsize=18)
    plt.xlim(-7, 7)
    plt.ylim(-1.1,1.1)
    plt.grid(True)
    plt.show()
