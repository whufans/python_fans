#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 14:28
# @Author  : fans
# @File    : readConfig.py
# @Software: PyCharm Community Edition
import configparser
class ReadConfig:
	@staticmethod
	def readConfig(fileName,section,option):
		cf = configparser.RawConfigParser()
		cf.read(fileName,encoding='utf-8')
		value=cf.get(section,option)
		return value
