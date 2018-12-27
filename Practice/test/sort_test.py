#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 10:54
# @Author  : fans
# @File    : sort_test.py
# @Software: PyCharm Community Edition

def select_sort(array):
	assert type(L) == type(['']), "输入的参数不是列表"
	for i in range(len(array)):
		x = i  # min index
		for j in range(i, len(array)):
			if array[j] < array[x]:
				x = j
		array[i], array[x] = array[x], array[i]
	return array

L=[]
print(select_sort(L))