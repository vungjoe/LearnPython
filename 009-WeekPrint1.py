#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：输入1-7，输出对应的星期几。比如，输入5，输出星期五。
'''

WeekAll="星期一星期二星期三星期四星期五星期六星期日"
a=input('输入数字1-7中的一个：')
b=eval(a)
print(WeekAll[(b-1)*3:b*3])