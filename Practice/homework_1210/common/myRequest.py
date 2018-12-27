#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 10:01
# @Author  : fans
# @File    : myRequest.py
# @Software: PyCharm Community Edition
import  requests
class MyRequest:
	def  myRequest(self,http_method,url,data,cookies=None):
		if http_method=='get':
			res=requests.get(url,data)
		elif http_method=='post':
			res = requests.post(url, data,cookies=cookies)
		else:
			print("请求方式错误")
		return res