#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 10:12
# @Author  : fans
# @File    : testAPI.py
# @Software: PyCharm Community Edition
import unittest

from ddt import ddt, data

from  homework_1210.common.doExcel import DoExcel
from homework_1210.common.myLogger import MyLogger
from homework_1210.common.myRequest import MyRequest
from homework_1210.common import getFilePath
test_data=DoExcel(getFilePath.testDataPath,'Sheet1').doExcel()
logger=MyLogger('log')
logger.info('test_data:{}'.format(test_data))
COOKIE=None
@ddt
class TestAPI(unittest.TestCase):
	def setUp(self):
		self.t=DoExcel(getFilePath.testDataPath,'Sheet1')

	@data(*test_data)
	def test_api(self,item):
		global COOKIE
		logger.info("---------------------")
		logger.info("正在执行第{}条用例".format(item['id']))
		logger.info("---------开始检查请求方式-----------")
		logger.info("请求方式为{},数据类型是{}".format(item['http_method'],type(item['http_method'])))
		logger.info("---------开始检查URL地址-----------")
		logger.info("URL地址为{},数据类型是{}".format(item['url'], type(item['url'])))
		logger.info("---------开始检查输入参数-----------")
		logger.info("输入参数为{},数据类型是{}".format(item['data'], type(item['data'])))
		logger.info("---------开始检查预期结果-----------")
		logger.info("预期结果为{},数据类型是{}".format(item['expected'], type(item['expected'])))
		res=MyRequest().myRequest(item['http_method'],item['url'],eval(item['data']),COOKIE)
		logger.info("---------开始检查输出结果-----------")
		logger.info("输出结果为{},数据类型是{}".format(res.json(), type(res.json())))
		if res.cookies:
			COOKIE = res.cookies
		try:
			self.assertEqual(str(item['expected']),res.json()['code'])
			TestResult='PASS'
			logger.info("测试结果为{}".format(TestResult))
		except AssertionError as e:
			logger.info("断言错误是{}".format(e))
			TestResult = 'FAIL'
			logger.error("测试结果为{}".format(TestResult))
			raise  e
		finally:
			self.t.writeBack(item['id']+1,7,str(res.json()))
			self.t.writeBack(item['id'] + 1, 8, TestResult)
