#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:26
# @Author  : fans
# @File    : testCase.py
# @Software: PyCharm Community Edition
import unittest
from   homework_1203.myrequest  import MyRequest
COOKIES=None
class TestMethod(unittest.TestCase):
	def __init__(self,methodName,http_method,url,data,expected):
		super(TestMethod,self).__init__(methodName)
		self.http_method=http_method
		self.url=url
		self.data=data
		self.expected=expected

	def test_api(self):
		global COOKIES
		res=MyRequest().myRequest(self.http_method,self.url,self.data,COOKIES)
		actual=res.json()['code']
		print(res.json())
		if res.cookies:
			COOKIES=res.cookies
		try:
			self.assertEqual(self.expected,actual)
		except AssertionError as e:
			print("断言错误：{}".format(e))
			raise  e