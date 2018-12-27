#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 14:00
# @Author  : fans
# @File    : suite&runner.py
# @Software: PyCharm Community Edition
import HTMLTestRunnerNew
import unittest
from homework_1210.common import getFilePath
from homework_1210.common import testAPI

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testAPI))
with open(getFilePath.testReportPath,'wb+') as file:
	runner=HTMLTestRunnerNew.HTMLTestRunner(file, verbosity=2,title='接口测试报告',description='fans的接口测试报告',tester='fans')
	runner.run(suite)

