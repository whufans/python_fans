#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 14:54
# @Author  : fans
# @File    : suite&runner.py
# @Software: PyCharm Community Edition
import unittest
import  HTMLTestRunnerNew
from homework_1130 import testCase
suite=unittest.TestSuite()
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(testCase))
# with open('testResult.txt','w+') as file:
# 	runner=unittest.TextTestRunner(file, descriptions='测试报告', verbosity=2)
# 	runner.run(suite)

suite.addTest(loader.loadTestsFromTestCase(testCase.TestMyRequest))
with open('testReport.html','wb+') as file2:
	runner2=HTMLTestRunnerNew.HTMLTestRunner(stream=file2, verbosity=2,title='登录充值测试报告',description='fans的登录充值测试报告',tester='fans')
	runner2.run(suite)