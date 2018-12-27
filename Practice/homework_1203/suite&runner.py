#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:26
# @Author  : fans
# @File    : suite&runner.py
# @Software: PyCharm Community Edition
import  unittest
import HTMLTestRunnerNew
from homework_1203.do_excel import Do_excel
from homework_1203.testCase import TestMethod
test_data=Do_excel('test.xlsx','Sheet1').do_excel()
suite=unittest.TestSuite()
loader=unittest.TestLoader()
for item in test_data:
	if  item['expected']=='None':
		suite.addTest(TestMethod('test_api', item['http_method'], item['url'], eval(item['data']), eval(item['expected'])))
	else:
		suite.addTest(TestMethod('test_api',item['http_method'],item['url'],eval(item['data']),str(item['expected'])))
with open('test.html','wb+') as file:
	runner = HTMLTestRunnerNew.HTMLTestRunner(file, verbosity=2,title='测试报告',description='fans的测试报告',tester='fans')
	runner.run(suite)
# with open('test.txt','w+') as file:
# 	runner = unittest.TextTestRunner(file,verbosity=2)
# 	runner.run(suite)
