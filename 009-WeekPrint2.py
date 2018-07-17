#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：输入1-7，输出对应的星期几。比如，输入5，输出星期五。
'''

WeekAll="一二三四五六日"
WeekID=eval(input('输入数字1-7中的一个：'))
print('星期' + WeekAll[WeekID - 1])