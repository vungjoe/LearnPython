#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：

第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
'''

N = eval(input('请输入一个奇数：'))
n = N % 2
if n == 1:
	for i in range(1,N+2,2):
		StarNum = '*' * i
		print(StarNum.center(N))
else:
	print('你输入的不是奇数。')