#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 12:20
# @Author  : fans
# @File    : homework_1126.py
# @Software: PyCharm Community Edition
# 1：自己写一个工具类，完成数学的加减乘除以及平方积操作
# 2：对每个方法写2个用例
# 3：针对测试用例选用不同的方法去执行，然后生成测试报告
import unittest
from homework.ToolClass_1126  import  ToolClass
class TestToolClass(unittest.TestCase):
	#加法的测试用例：2个正数相加，2个负数相加。
	@classmethod
	def setUpClass(cls):
		print("连接数据库，连接数据库成功。")
	@classmethod
	def tearDownClass(cls):
		print("关闭数据库。")

	# 加法的测试用例：2个正数相加，2个负数相加。
	def test_add_twopositive(self):
		expected=6
		actual=ToolClass().add(2,3)
		print("加法的测试用例：2个正数相加。")
		try:
			self.assertEqual(expected,actual)
		except AssertionError as e:
			print('报错为：{}'.format(e))
			# raise  e

	def test_add_two_negtive(self):
		expected = -7
		actual = ToolClass().add(-4, -3)
		print("加法的测试用例：2个负数相加。")
		self.assertEqual(expected,actual)

	# 减法的测试用例：2个正数相减，2个负数相减。
	def test_sub_twopositive(self):
		expected=2
		actual=ToolClass().subtract(5,3)
		print("减法的测试用例：2个正数相减。")
		self.assertEqual(expected,actual)

	def test_sub_two_negtive(self):
		expected = -1
		actual = ToolClass().subtract(-4, -3)
		print("减法的测试用例：2个负数相减。")
		self.assertEqual(expected,actual)

	# 乘法的测试用例：2个正数相乘，2个负数相乘。
	def test_multiple_twopositive(self):
		expected=15
		actual=ToolClass().multiple(5,3)
		print("乘法的测试用例：2个正数相乘。")
		self.assertEqual(expected,actual)

	def test_multiple_two_negtive(self):
		expected = 12
		actual = ToolClass().multiple(-4, -3)
		print("乘法的测试用例：2个负数相乘。")
		self.assertEqual(expected,actual)

	#除法的测试用例：2个正数相除，2个负数相除。
	def test_divide_twopositive(self):
		expected=3
		actual=ToolClass().divide(9,3)
		print("除法的测试用例：2个正数相除。")
		self.assertEqual(expected,actual)

	def test_divide_two_negtive(self):
		expected = 2
		actual = ToolClass().divide(-4, -2)
		print("除法的测试用例：2个负数相除。")
		self.assertEqual(expected,actual)

	# 平方积的测试用例：2个正数平方积，2个负数平方积。
	def test_squareProduct_twopositive(self):
		expected = 36
		actual = ToolClass().squareProduct(2, 3)
		print("平方积的测试用例：2个正数平方积。")
		self.assertEqual(expected,actual)

	def test_squareProduct_two_negtive(self):
		expected = 64
		actual = ToolClass().squareProduct(-4, -2)
		print("平方积的测试用例：2个负数平方积。")
		self.assertEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()


