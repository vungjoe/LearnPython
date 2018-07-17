#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
天天向上之工作日的力量：
假设工作日每天进步1%，休息日每天退步1%。一年365天之后会时什么样的呢？
'''

DayFinal = 1
dayfactor = 0.01
for i in range(1,365):
	if i % 7 in [0,6]:
		DayFinal = DayFinal * ( 1 - dayfactor )
	else:
		DayFinal = DayFinal * ( 1 + dayfactor )

print("工作日的力量结果：{:.2f}".format(DayFinal))