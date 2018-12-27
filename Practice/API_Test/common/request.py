#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 12:21
# @Author  : fans
# @File    : request.py
# @Software: PyCharm Community Edition
import  requests
class Request:
	def __init__(self,method,url,data=None,cookies=None,headers=None):
		try:
			if method.upper=='GET':
				self.resp=requests.get(url=url,params=data,cookies=cookies,headers=headers)
			elif method.upper=='POST':
				self.resp=requests.post(url=url,data=data,cookies=cookies,headers=headers)
			elif method.upper=='PUT':
				self.resp=requests.put(url=url,data=data,cookies=cookies,headers=headers)
			elif method.upper=='OPTIONS':
				self.resp=requests.options(url=url,params=data,cookies=cookies,headers=headers)
			elif method.upper=='HEAD':
				self.resp=requests.head(url=url,params=data,cookies=cookies,headers=headers)
			elif method.upper=='PATCH':
				self.resp=requests.patch(url=url,data=data,cookies=cookies,headers=headers)
			elif method.upper=='DELETE':
				self.resp=requests.delete(url=url,params=data,cookies=cookies,headers=headers)
		except Exception as e:
			print("请求报错")
			raise e

	def get_status_code(self):
		return self.resp.status_code

	def get_headers(self):
		return self.resp.headers

	def get_text(self):
		return self.resp.text

	def get_json(self):
		return self.resp.json()

	def get_cookies(self):
		return self.resp.cookies
if __name__ == '__main__':
	method='get'
	url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
	data={'mobilephone': 18688773467, 'pwd': '123456'}
	res=Request(method,url,data)
	print(res.get_text())