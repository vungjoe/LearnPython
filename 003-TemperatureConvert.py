#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
温度的刻画有两个不同体系：摄氏度（Celsius）和华氏度（Fabrenheit）。

请编写程序将用户输入华氏度转换为摄氏度，或将输入的摄氏度转换为华氏度。

转换算法如下：（C表示摄氏度、F表示华氏度）

         C = ( F - 32 ) / 1.8

         F = C * 1.8 + 32

要求如下：

(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；

(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指摄氏度87.65度；

(3) 不考虑异常输入的问题，输出保留小数点后两位；

(4) 使用input()获得测试用例输入时，不要增加提示字符串。
'''

Temp = input()
if Temp[0] == 'C':
	TempC = eval(Temp[1:])
	TempF = TempC * 1.8 + 32
	print("F" + "{:.2f}".format(TempF));
elif Temp[0] == 'F':
	TempF = eval(Temp[1:])
	TempC = (TempF -32) / 1.8
	print("C" + "{:.2f}".format(TempC))
else:
	print('Inleagal input,please try again.')
