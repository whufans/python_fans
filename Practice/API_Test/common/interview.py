#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 16:28
# @Author  : fans
# @File    : interview.py
# @Software: PyCharm Community Edition
import  os
import hashlib
# 01 文件名去重复
# 02 选出文件大于10m的
# 03 获取到文件的md5值，然后利用这个md5值对文件名进行重命名（其中md5代表一个文件属性）
# 04 打印出最后的符合条件的所有文件名
class FileChoose:
	def __init__(self,path):
		self.files = []
		for root, dirs, files in os.walk(path):
			for file in files:
				apath = os.path.join(root, file)
				self.files.append(apath)

	def filter_size_filter(self,files,filter_size=10):
			new_files=[]
			for file in files:
				file_size = os.path.getsize(file)/1024/1024
				if file_size<filter_size:
					new_files.append(file)
			return new_files
	def filter_type_filter(self,files,filter_type=None):
			new_files=[]
			for file in files:
				ext = os.path.splitext(file)[1]
				if filter_type :
					if ext in filter_type:
						new_files.append(file)
				else:
					return files
			return  new_files

	def del_dulplicate(self,files):
		the_list=[]
		the_set=set()
		for file in files :
			file_name=os.path.split(file)[1]
			if file_name not in the_set:
				the_set.add(file_name)
				the_list.append(file)
		return the_list

	def MD5_Rename(self,files):
		for file in files:
			dx = hashlib.md5()
			with open(file, 'rb') as f:
				b = f.read()
				dx.update(b)
			newname = dx.hexdigest()
			filename=newname+os.path.splitext(file)[1]
			new_path=os.path.join(os.path.dirname(file),filename)
			os.renames(file,new_path)


if __name__ == '__main__':
	result=FileChoose(r"E:\test")
	size_filter_files=result.filter_size_filter(result.files)
	type_filter_file=result.filter_type_filter(result.files,'.pdf')
	del_dulplicate_file=result.del_dulplicate(size_filter_files)
	result.MD5_Rename(del_dulplicate_file)

