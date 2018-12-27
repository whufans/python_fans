#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 12:38
# @Author  : fans
# @File    : homework_1130.py
# @Software: PyCharm Community Edition
# 1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
# 2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
# 温馨提示：可以用到全部变量，global
#登录地址和数据
# login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# login_data={'mobilephone':18688773467,'pwd':'123456'}
# #充值地址和数据
# recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
# recharge_data={'mobilephone':18688773467,'amount':'1000'}
import  requests
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
class myRequest:
	def  myrequest(self,method_name,url,data,cookies=None):
		if method_name=='get':
			res=requests.get(url,data)
		elif method_name=='post':
			res=requests.post(url,data,cookies=cookies)
		else:
			print("您输入的方法有问题。")
		return res
res=requests.get(login,login_data)
print(res.json(),res.headers,res.status_code)
print(res.text)
print(res.json()['msg'])
cookie=res.cookies
print(res.request.url,res.request.headers)
res_recharge=requests.post(recharge,recharge_data,cookies=cookie)
# res_recharge=requests.post(recharge,recharge_data)
print(res_recharge.json())
print(res_recharge.json()['msg'])