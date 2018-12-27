#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 18:28
# @Author  : fans
# @File    : python1109.py
# @Software: PyCharm Community Edition
# 1：一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
def totalPersonNum(x,y,k):
	total = 0
	for i in range(k):
		age=int(input("请输入你的年龄"))
		gender = input("请输入你的性别")
		if  x<=age<=y  and  gender=='f':
			total+=1
	print("满足条件的总人数是{}".format(total))
# 2：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def judgeLength(item):
	if isinstance(item,list) or isinstance(item,str) or isinstance(item,tuple):
		return (len(item)>5)
boolean=judgeLength("1234567")
print(boolean)
boolean=judgeLength("1234")
print(boolean)
boolean=judgeLength([1,2,3,4,5,6,7])
print(boolean)
boolean=judgeLength([1,2,3,4])
print(boolean)
boolean=judgeLength((1,2,3,4,5,6,7))
print(boolean)
boolean=judgeLength((1,2,3,4))
print(boolean)
# 3、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def  handleList(args):
	if len(args)>2 and isinstance(args,list):
		return   args[0:2]
list1=handleList([1,2,3,4,5])
print(list1)
# 4、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。
def  judgeStr(str,dict):
	if str not in dict.values():
		dict[str]=str
	return dict
print(judgeStr('23',{1:"12",2:"23"}))
