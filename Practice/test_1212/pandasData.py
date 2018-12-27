#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 12:46
# @Author  : fans
# @File    : pandasData.py
# @Software: PyCharm Community Edition
# import  pandas as pd
# 一、pandas操作Excel表单
#方法一：默认读取第一个表单
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出
#方法二：通过指定表单名的方式来读取
# df=pd.read_excel('lemon.xlsx',sheet_name='student')#可以通过sheet_name来指定读取的表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出
#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
# df=pd.read_excel('lemon.xlsx',sheet_name=['python','student'])#可以通过表单名同时指定多个
# df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
# data=df.values#获取所有的数据，注意这里不能用head()方法哦~
# print("获取到所有的值:\n{0}".format(data))#格式化输出
# 二、pandas操作Excel的行列
#1：读取指定的单行，数据会存在列表里面
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.ix[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
# print("读取指定行的数据：\n{0}".format(data))
# 2：读取指定的多行，数据会存在嵌套的列表里面：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[[1,2]].values#读取指定多行的话，就要在ix[]里面嵌套列表指定行数
# print("读取指定行的数据：\n{0}".format(data))
# 3：读取指定的行列：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[1,2]#读取第一行第二列的值，这里不需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))
# 4：读取指定的多行多列值：
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[[1,2],['title','data']].values#读取第一行第二行的title以及data列的值，这里需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))
# 5：获取所有行的指定列
# df=pd.read_excel('lemon.xlsx')
# data=df.ix[:,['title','data']].values#读所有行的title以及data列的值，这里需要嵌套列表
# print("读取指定行的数据：\n{0}".format(data))
# 6：获取行号并打印输出
# df=pd.read_excel('lemon.xlsx')
# print("输出行号列表",df.index.values)
# 7：获取列名并打印输出
# df=pd.read_excel('lemon.xlsx')
# print("输出列标题",df.columns.values)
# 8：获取指定行数的值：
# df=pd.read_excel('lemon.xlsx')
# print("输出值",df.sample(3).values)#这个方法类似于head()方法以及df.values方法
# 9：获取指定列的值：
# df=pd.read_excel('lemon.xlsx')
# print("输出值\n",df['data'].values)
# 三：pandas处理Excel数据成为字典
import  pandas as pd
df=pd.read_excel('test.xlsx')
df.ix[10,10].values='asd'