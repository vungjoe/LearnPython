#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
计算π的值，有两种方案：

- 公式法
- 随机投点法（蒙特卡罗算法）

'''

import random
import time

# 方法一：选择其中一种公式来计算
pi = 0
N = 100
for k in range(N):
	pi = pi + 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("公式法计算出的圆周率的值是：{}".format(pi))

# 方法二：随机数求解

DARTS = 1000*1000*10
hits = 0.0
start = time.perf_counter()
for i in range(DARTS):
	x,y = random.random(),random.random()
	dist = pow(x**2+y**2,0.5)
	if dist < 1:
		hits = hits + 1
pi = 4 * ( hits / DARTS )
print("蒙特卡罗法计算出的圆周率的值是：{}".format(pi))
print("程序的运行时间是：{:.5f}s".format(time.perf_counter()-start))
