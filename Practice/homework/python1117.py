#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 10:44
# @Author  : fans
# @File    : python1117.py
# @Software: PyCharm Community Edition
# 1：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。在类
# User中定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()
# 的方法，它向用户发出个性化的问候。 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User:
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
	def describe_user(self):
		print("用户姓名是{}{}".format(self.first_name,self.last_name))
	def greet_user(self):
		print("{}{}用户，欢迎您！".format(self.first_name,self.last_name))
user1=User("张","强")
user2=User("关","羽")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
# 2：定义一个学生类。
# 1）有下面的类属性： 1姓名2年龄3成绩（语文，数学，英语)[每课成绩的类型为整数], 均放在初始化函数里面。
# 2）类方法：
# a)获取学生的姓名：get_name()返回类型: str
# b)获取学生的年龄：get_age()返回类型: int
# c) 返回3门科目中最高的分数。get_course()返回类型: int
# 写好类以后，可以定义2个同学测试下: zm = Student('zhangming', 20, [69, 88, 100])返回结果： zhangming 20 100
class Student:
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def get_course(self):
		return max(self.score)
zm=Student('zhangming', 20, [69, 88, 100])
print("姓名：{}，年龄：{}，三门科目的最好成绩：{}。".format(zm.get_name(),zm.get_age(),zm.get_course()))
hh=Student('huahua', 18, [56, 91, 23])
print("姓名：{}，年龄：{}，三门科目的最好成绩：{}。".format(hh.get_name(),hh.get_age(),hh.get_course()))
# 3.人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1曹操2张飞3刘备
# 2）函数2：角色猜拳1剪刀2石头3布玩家输入一个1 - 3的数字
# 3）函数3：电脑出拳随机产生1个1 - 3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输, 然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果角色赢几局电脑赢几局，平局几次游戏结束
import random
class Game:
	def selectrole(self):
		roleid=int(input("请选择角色：1曹操、2张飞、3刘备。"))
		return roleid
	def role_guess(self):
		r_guess=int(input("请猜拳：1剪刀、2石头、3布。"))
		return r_guess
	def computer_guess(self):
		c_guess=random.randint(1,3)
		guess_list = ["剪刀", "石头", "布"]
		print("电脑的猜拳结果是{}".format(guess_list[c_guess-1]))
		return c_guess
	def battle(self):
		even =0
		r_win=0
		c_win=0
		flag = "y"
		role_list = ["曹操", "张飞", "刘备"]
		role=role_list[self.selectrole()-1]
		while(flag=="y"):
			r_guess=self.role_guess()
			c_guess=self.computer_guess()
			if(r_guess==c_guess):
				print("本局对战结果： 平局")
				even+=1
			elif((r_guess==2 and c_guess==1 ) or (r_guess==3 and c_guess==2 ) or (r_guess==1 and c_guess==3 ) ):
				print("本局对战结果： 赢")
				r_win+=1
			else:
				print("本局对战结果： 输")
				c_win += 1
			flag=input("是否继续？按y继续，按n退出")
		print("{}赢{}局,电脑赢{}局，平局{}次".format(role,r_win,c_win,even))
game=Game()
game.battle()
# 4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
# 1)平日票价100元
# 2)周末票价为平日票价120 %
# 3)儿童半价
from time import time,localtime,strftime
class Ticket:
	def __init__(self,children,adult):
		self.children=children
		self.adult=adult
	def  get_current_oneticket_price(self):
		current_time = strftime("%A", localtime(time()))
		weekend = ["Saturday", "Sunday"]
		if current_time in weekend:
			return    120
		else:
			return    100
	def  get_total_price(self):
		total_price=self.get_current_oneticket_price()*(self.children*0.5+self.adult)
		return total_price
ticket1=Ticket(2,6)
print("总票价是{}".format(ticket1.get_total_price()))
# 拓展题：只提供源码，上课不做讲解~有兴趣的可以找老师讨论
# 5：购物车类，包含的功能如下，请自行设计这个类以及类里面的方法:
# 1)用户输入工资后，打印商品列表（商品列表自行设计展示模式）
# 2）允许用户根据商品编号去选择商品
# 3)用户选择商品后，检查余额是否足够，够的话直接扣款，不够的话就对用户做出提醒
# 4）用户可以随时退出，退出时打印用户的购买商品以及余额
