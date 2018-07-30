#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
天天向上之工作日的力量：
假设有两个人，A 君每天进步1%；
B 君休息日每天退步1%，则B 君工作日需多努力才能和A 君达到同样的效果？
周期仍为一年（365天）。

方法：笨办法试错。利用计算机高速的运算速度来不断地试错，直至符合要求。
'''

# def 保留字用于定义一个函数

def dayup(df):
	dayup = 1
	for i in range(365):
		if i % 7 in [0,6]:
			dayup = dayup * ( 1 - 0.01 )
		else:
			dayup = dayup * ( 1 + df )
	return dayup

dayfactor = 0.01
while dayup(dayfactor) < 37.78:
	dayfactor += 0.001

print("工作日的力量结果：{:.3f}".format(dayfactor))