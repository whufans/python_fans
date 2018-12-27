#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 14:19
# @Author  : fans
# @File    : testCase.py
# @Software: PyCharm Community Edition
import  unittest
from ddt import ddt,data
from  homework_1130.myRequest import  MyRequest
from  homework_1130.do_excel import  DoExcel
test_data=DoExcel('test.xlsx','Sheet1').do_excel()
print(test_data)
@ddt
class  TestMyRequest(unittest.TestCase):
	# def setUp(self):
	# 	print('连接数据库......，连接数据库成功。')
	# def tearDown(self):
	# 	print('关闭数据库连接。')
	#输入正确的用户名和密码登录
	@data(*test_data)
	def test_get_success(self,data_item):
		expected='登录成功'
		res=MyRequest().myrequest('get',data_item['url'],data_item['data'])
		# actual=res.json()['msg']
		print(res.json())
		print(test_data)
		# self.assertEqual(expected,actual)
