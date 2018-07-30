#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
一年365天，以第1天的能力值为基数，记为1.0。

当好好学习时，能力值相比前一天提高N‰；当没有学习时，能力值相比前一天下降N‰。

每天努力或放任，一年下来的能力值相差多少呢？其中，N的取值范围是0到100，N可以是小数，假设输入符合要求。

获得用户输入的N，计算每天努力和每天放任365天后的能力值及能力间比值，其中，能力值保留小数点后2位，能力间比值输出整数，输出结果间采用英文逗号分隔。

使用input()获得N。
'''

N = eval(input())
DayDayUp = 1.0*pow(1+N/1000,365)
DayDayDown = 1.0*pow(1-N/1000,365)
consult = DayDayUp//DayDayDown
print('{:.2f},{:.2f},{:.0f}'.format(DayDayUp,DayDayDown,consult))