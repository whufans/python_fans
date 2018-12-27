#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 12:46
# @Author  : fans
# @File    : pandasData.py
# @Software: PyCharm Community Edition
# import  pandas as pd
# 一、pandas操作Excel表单
#方法一：默认读取第一个表单
#方法二：通过指定表单名的方式来读取
#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
#可以通过表单名同时指定多个
#可以通过表单索引来指定读取的表单
#可以混合的方式来指定
#可以通过索引 同时指定多个
#获取所有的数据，注意这里不能用head()方法哦~

# 二、pandas操作Excel的行列
#1：读取指定的单行，数据会存在列表里面
# 表示第一行 这里读取数据并不包含表头，要注意哦！
# 2：读取指定的多行，数据会存在嵌套的列表里面：
#读取指定多行的话，就要在ix[]里面嵌套列表指定行数
# 3：读取指定的行列：
#读取第一行第二列的值，这里不需要嵌套列表
# 4：读取指定的多行多列值：
#读取第一行第二行的title以及data列的值，这里需要嵌套列表
# 5：获取所有行的指定列
#读所有行的title以及data列的值，这里需要嵌套列表
# 6：获取行号并打印输出
# 7：获取列名并打印输出
# 8：获取指定行数的值：
#这个方法类似于head()方法以及df.values方法
# 9：获取指定列的值：
# 三：pandas处理Excel数据成为字典
# df=pd.read_excel('lemon.xlsx')
# test_data=[]
# for i in df.index.values:#获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
#     row_data=df.ix[i,['case_id','module','title','http_method','url','data','expected']].to_dict()
#     test_data.append(row_data)
# print("最终获取到的数据是：{0}".format(test_data))