#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 17:40
# @Author  : fans
# @File    : python1105_for.py
# @Software: PyCharm Community Edition
# 1：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）
# 和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
total = 0
for i in range(10):
	gender =  input("请输入你的性别：m表示男性，f表示女性")
	age = int(input("请输入你的年龄："))
	if gender == 'f' and   10<=age<=12:
		total+=1
print("满足条件的总人数是{}".format(total))
# 2：利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
a=[1,7,4,89,34,2]
aLength=len(a)
for i in range(aLength-1):
	for j in range(aLength-i-1):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
print(a)
# 3： 万科笔试题：
# 有一组用户的登录信息存储在字典 login_ifno 里面，字典格式如下：login_info={"admin":"root","user_1":"123456"}
# key表示用户名，value表示密码，请编写函数满足如下条件：
# 1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
# 2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名
# 3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
# 4)如果密码输入错误超过三次，中断程序运行。
# 5)当输入密码错误时，提示还有几次机会
# 6)用户名和密码都输入正确的时候，提示登陆成功!'''
login_info={"admin":"root","user_1":"123456"}
flag=0
key=input("请输入登录的用户名")
while True:
	if  key  in login_info :
		break
	else:
		key = input("请输入正确的用户名")
for i in range(1,4):
	value=input("请输入密码")
	if value == login_info[key]:
		print("登陆成功")
		break
	else :
		print("还有{}次机会".format(3-i))




