#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
题目要求：编写一个程序，计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔。

其中：N是一个整数或浮点数。
'''

a = input()
c = eval(a)
b = [1] * 6
b[0] = c ** 0
b[1] = c ** 1
b[2] = c ** 2
b[3] = c ** 3
b[4] = c ** 4
b[5] = c ** 5

print(" ".join(str(i) for i in b)) 
