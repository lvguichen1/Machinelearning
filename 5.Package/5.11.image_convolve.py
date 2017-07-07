#!/usr/bin/python
# -*- coding:utf-8 -*-


import numpy as np
import os
from PIL import Image


def convolve(image, weight):
    height, width = image.shape
    print height, width
    h, w = weight.shape
    height_new = height - h + 1
    width_new = width - w + 1
    image_new = np.zeros((height_new, width_new), dtype=np.float)
    for i in range(height_new):
        for j in range(width_new):
            image_new[i, j] = np.sum(image[i:i + h, j:j + w] * weight)
    image_new = image_new.clip(0, 255)
    image_new = np.rint(image_new).astype('uint8')
    return image_new


if __name__ == '__main__':
    A = Image.open('son.png', 'r')
    output_path = '.\\ImageConvolve\\'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    a = np.array(A)
    print a
    avg3 = np.ones((3, 3))
    avg3 /= avg3.sum()
    avg5 = np.ones((5, 5))
    avg5 /= avg5.sum()
    gauss = np.array(([0.003, 0.013, 0.022, 0.013, 0.003],
                      [0.013, 0.059, 0.097, 0.059, 0.013],
                      [0.022, 0.097, 0.159, 0.097, 0.022],
                      [0.013, 0.059, 0.097, 0.059, 0.013],
                      [0.003, 0.013, 0.022, 0.013, 0.003]))
    soble_x = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))
    soble_y = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]))
    soble = np.array(([-1, -1, 0], [-1, 0, 1], [0, 1, 1]))
    prewitt_x = np.array(([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    prewitt_y = np.array(([-1, -1, -1], [0, 0, 0], [1, 1, 1]))
    prewitt = np.array(([-2, -1, 0], [-1, 0, 1], [0, 1, 2]))
    laplacian4 = np.array(([0, -1, 0], [-1, 4, -1], [0, -1, 0]))
    laplacian8 = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]))
    weight_list = (
    'avg3', 'avg5', 'gauss', 'soble_x', 'soble_y', 'soble', 'prewitt_x', 'prewitt_y', 'prewitt', 'laplacian4',
    'laplacian8')
    print '梯度检测'
    for weight in weight_list:
        print weight, 'R'
        R = convolve(a[:, :, 0], eval(weight))
        print a[:, :, 0]
        print 'G'
        G = convolve(a[:, :, 1], eval(weight))
        print a[:, :, 1]
        print 'B'
        B = convolve(a[:, :, 2], eval(weight))
        print a[:, :, 2]
        I = np.stack((R, G, B), 2)
        Image.fromarray(I).save(output_path + weight + '.png')
