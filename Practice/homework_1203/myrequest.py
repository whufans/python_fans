#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:27
# @Author  : fans
# @File    : myrequest.py
# @Software: PyCharm Community Edition
import  requests
class MyRequest:
	def  myRequest(self,method_name,url,data,cookies):
		if method_name=='get':
			res=requests.get(url,data)
		elif method_name=='post':
			res=requests.post(url,data,cookies=cookies)
		else:
			print("发起的请求方式存在问题")
		return  res
	# def  myRequest(self,method_name,url,data,cookies):
	# 	try:
	# 		res=requests.request(method_name,url,params=data,cookies=cookies)
	# 	except Exception as e:
	# 		res=print("发起的请求方式存在问题",e)
	# 	return res



