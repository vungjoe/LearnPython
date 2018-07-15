#!/usr/bin/pyhton
# -*- coding:utf-8 -*-

'''
获得用户输入的一个整数N，计算N的平方值；结果采用宽度20字符方式居中输出，空余字符采用减号(-)填充。
如果结果超过20个字符，则以结果宽度为准。
'''

N = input('Please input a integer:')
i = 20
SqureOfN = eval(N) ** 2
LengthOfSqure = len(str(SqureOfN))
if LengthOfSqure > 20:
    print(SqureOfN)
else:
    NumOfMiners = i - LengthOfSqure

    print()
