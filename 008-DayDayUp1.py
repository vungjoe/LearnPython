#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
天天向上之工作日的力量：
假设工作日每天进步1%，休息日每天退步1%。一年365天之后会时什么样的呢？
'''

dayfactor = 0.01
DaySum = 365
UpDayLast = DaySum % 7
if UpDayLast < 5:
	DownDayLast = 0
else:
	DownDayLast = 7 - UpDayLast
UpCount = DaySum // 7 * 5 + UpDayLast
DownCount = DaySum // 7 * 2 + DownDayLast
DayDayUp = pow(1+dayfactor,UpCount)
DayDayDown = pow(1-dayfactor,DownCount)
print("{:.2f}".format(DayDayUp*DayDayDown))