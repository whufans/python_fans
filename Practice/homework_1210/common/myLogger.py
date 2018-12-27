#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 14:33
# @Author  : fans
# @File    : myLogger.py
# @Software: PyCharm Community Edition
import logging

from homework_1210.common.readConfig import ReadConfig
from homework_1210.common import getFilePath


class MyLogger:
	def __init__(self,logName):
		self.logName=logName

	def myLogger(self,msg,level):
		logLevel = ReadConfig.readConfig(getFilePath.confPath,'Log','logLevel')
		ConsoleButton = ReadConfig.readConfig(getFilePath.confPath,'Log','ConsoleButton')
		ConsoleLevel = ReadConfig.readConfig(getFilePath.confPath,'Log','ConsoleLevel')
		FileButton = ReadConfig.readConfig(getFilePath.confPath,'Log','FileButton')
		FileLevel = ReadConfig.readConfig(getFilePath.confPath,'Log','FileLevel')
		format =ReadConfig.readConfig(getFilePath.confPath,'Log','format')

		logger=logging.getLogger(self.logName)
		logger.setLevel(logLevel)
		formatter=logging.Formatter(format)
		if ConsoleButton=='ON':
			ch=logging.StreamHandler()
			ch.setLevel(ConsoleLevel)
			ch.setFormatter(formatter)
			logger.addHandler(ch)

		if FileButton=='ON':
			ch2=logging.FileHandler(getFilePath.logPath, encoding='utf-8')
			ch2.setLevel(FileLevel)
			ch2.setFormatter(formatter)
			logger.addHandler(ch2)

		if  level=='DEBUG':
			logger.debug(msg)
		elif  level=='INFO':
			logger.info(msg)
		elif  level=='WARNING':
			logger.warning(msg)
		elif  level=='ERROR':
			logger.error(msg)
		elif  level=='CRITICAL':
			logger.critical(msg)

		logger.removeHandler(ch)
		logger.removeHandler(ch2)

	def debug(self,msg):
		self.myLogger(msg,'DEBUG')
	def info(self,msg):
		self.myLogger(msg,'INFO')
	def warning(self,msg):
		self.myLogger(msg,'WARNING')
	def error(self,msg):
		self.myLogger(msg,'ERROR')
	def critical(self,msg):
		self.myLogger(msg,'CRITICAL')


