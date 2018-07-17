#!/usr/bin/python3
# -*- coding:utf-8 -*-

import turtle as t

# Draw a squre.

for i in range(4):
	t.pencolor('red')
	t.pensize(4)
	t.fd(10)
	t.left(90)

# Draw a sixangle.

for i in range(1,7):
	t.pencolor('green')
	t.pensize(3)
	t.fd(20)
	t.left(60)

'''
使用turtle库，绘制一个叠边形，其中，叠边形内角为80度。
'''

for i in range(9):
	t.pencolor('blue')
	t.pensize(2)
	t.fd(40)
	t.left(80)

# 使用turtle库，绘制一个同切圆。

r=0
for i in range(4):
	t.pencolor('purple')
	t.pensize(1)
	r=r+20
	t.circle(r)
