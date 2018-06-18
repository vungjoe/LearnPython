#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：
请编写程序，完成米和英寸之间的长度转换，基本需求如下：
	输入英寸，转换成米；
	输入米，转换成英寸。

英寸采用in标记，放在数值结尾；米采用m标记，放在数值结尾。
	1 米 = 39.37 英寸

输入参数请使用input()，不要增加提示字符串信息。
'''

Length = input()
if Length[-1] == 'm':

	LengthMeter = eval(Length[:-1]) * 39.37
	print("{:.2f}".format(LengthMeter) + 'in')
elif Length[-1] == 'n':
	LengthInch = eval(Length[:-2]) / 39.37
	print("{:.2f}".format(LengthInch) + 'm')
else:
	print('Inleagal input,please try again.')
