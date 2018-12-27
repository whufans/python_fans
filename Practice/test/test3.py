#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 16:11
# @Author  : fans
# @File    : test3.py
# @Software: PyCharm Community Edition
import chardet
import base64
from suds.client import Client
from suds.transport.https import HttpAuthenticated  # webservice需要安全难证
user_url = "http://218.94.150.251:8070/court/service/SzftWebService?wsdl"
data_ry = {"Userid": "szft", "Pwd": "szftsa",
           "RequestXML": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8UmVxdWVzdD4KICAgIDxGSk0+UVRFdzwvRkpNPgo8L1JlcXVlc3Q+Cg=="}
client = Client(user_url)
# print(client)
# print(data_ry["Userid"],type(data_ry["Userid"]))
print(client.service.GetRy(RequestXML=data_ry["RequestXML"]))