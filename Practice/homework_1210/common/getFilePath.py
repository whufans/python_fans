#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 21:37
# @Author  : fans
# @File    : getFilePath.py
# @Software: PyCharm Community Edition
import os
from homework_1210.common.readConfig import ReadConfig
currentPath=os.path.realpath(__file__)
basePath=os.path.split(os.path.split(currentPath)[0])[0]
# case.conf  testReport.html  test.xlsx   mylog.txt
confPath=os.path.join(basePath,'conf','case.conf')
testReportPath=os.path.join(basePath,'testReport','testReport.html')
testDataPath=os.path.join(basePath,'testData','test.xlsx')
logPath=os.path.join(basePath,'log',ReadConfig.readConfig(confPath,'Log','FilePath'))
