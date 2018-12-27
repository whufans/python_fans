#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 12:41
# @Author  : fans
# @File    : suite_runner_1126.py
# @Software: PyCharm Community Edition
import unittest
import HTMLTestRunnerNew
from  homework import  homework_1126
suite=unittest.TestSuite()
loader=unittest.TestLoader()
#加载用例的三种方法:1、加载模块2、加载测试类3、加载测试类中的用例
suite.addTest(loader.loadTestsFromModule(homework_1126))
# suite.addTest(loader.loadTestsFromTestCase(homework_1126.TestToolClass))
# suite.addTest(homework_1126.TestToolClass('test_add_twopositive'))
#方法一：生成普通的测试报告，存放在TXT文件中
with open('testresult.txt','w+') as file :
	runner=unittest.TextTestRunner(file,descriptions="fans对工具类的测试结果", verbosity=2)
	runner.run(suite)

#方法二：生成HTML的测试报告，存放在HTML文件中
# with open('testresult.html','wb+') as file:
# 	runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="测试结果",description="fans对工具类的测试结果",tester="fans")
# 	runner.run(suite)