#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 10:39
# @Author  : fans
# @File    : random_array.py
# @Software: PyCharm Community Edition
from random import random
from json import dumps, loads


# 生成随机数文件
def dump_random_array(file='numbers.json', size=10 ** 4):
    fo = open(file, 'w', 1024)
    numlst = list()
    for i in range(size):
        numlst.append(int(random() * 10 ** 10))
    fo.write(dumps(numlst))
    fo.close()


# 加载随机数列表
def load_random_array(file='numbers.json'):
    fo = open(file, 'r', 1024)
    try:
        numlst = fo.read()
    finally:
        fo.close()
    return loads(numlst)