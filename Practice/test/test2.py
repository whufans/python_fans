#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:31
# @Author  : fans
# @File    : test2.py
# @Software: PyCharm Community Edition

# 1：L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# 打印Apple、Python、Lisa
# L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# print(L[0][0],L[1][1],L[2][2])
#
# # 2：完成列表a=[1,7,4,89,34,2]的冒泡排序（冒泡排序：小的排前面，大的排后面。），并写出冒泡的原理是什么？（很重要）
# #冒泡排序的原理：依次选取列表中第一个元素到倒数第二个元素作为被比较元素与列表其他元素进行比较，
# #如果被比较元素较大，将比较的两个元素进行互换
# a=[1,7,4,89,34,2]
# def bubbleSort(array):
# 	alength=len(array)
# 	if(alength==0 or alength==1):
# 		return  array
# 	for i in range(0,alength-1):
# 		for j in range(i+1,alength):
# 			if(array[i]>array[j]):
# 				array[i],array[j]=array[j],array[i]
# 	return array
# print(bubbleSort(a))
#
# # 3：利用input函数从控制台获取一个当前日期，如：20181031,然后利用自己所学知识，把他转换成 "2018年10月31号".
# currentTime=input("请以YYYYMMDD的格式输入当前时间，例如20181101")
# year=currentTime[0:4]
# month=currentTime[4:6]
# day=currentTime[-2:]
# print("{}年{}月{}号".format(year,month,day))
# print("%s年%s月%s号"%(year,month,day))
#
# # 4：复盘课堂的代码！一定要自己动手去操作！！
# str1="我的名字是"
# str2=' aaaFBA$@n#sdef!aa'
# print(str1+str2)
# print(str2.find('g',3,7))
# print(str2)
# print(str2.strip())
# print(str2.strip("a"))
# print(str2.find("aFBA"))
# print(str2.upper())
# print(str2.lower())
# print(str2.isupper())
# print(str2.islower())
# print(str2.isdigit())
# print(str2.replace('a','P',3))
str1='None'
print(eval(str1))





