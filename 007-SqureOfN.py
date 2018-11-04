#!/usr/bin/pyhton
# -*- coding:utf-8 -*-

'''
获得用户输入的一个整数N，计算N的平方值；结果采用宽度20字符方式居中输出，空余字符采用减号(-)填充。
如果结果超过20个字符，则以结果宽度为准。
'''

N = input('Please input a integer:')
SqureOfN = eval(N) ** 2

if len(str(SqureOfN)) < 20:
	print(str(SqureOfN).center(20,'-'))
else:
	print(SqureOfN)
