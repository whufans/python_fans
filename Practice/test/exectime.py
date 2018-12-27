#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 10:39
# @Author  : fans
# @File    : exectime.py
# @Software: PyCharm Community Edition
from _datetime import datetime


# 显示函数执行时间
def exectime(func):
    def inner(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(
            inter.seconds,
            inter.microseconds
        ))
        return result

    return inner