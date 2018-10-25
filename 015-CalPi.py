#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
����е�ֵ�������ַ�����

- ��ʽ��
- ���Ͷ�㷨�����ؿ����㷨��

'''

import random
import time

# ����һ��ѡ������һ�ֹ�ʽ������
pi = 0
N = 100
for k in range(N):
	pi = pi + 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("��ʽ���������Բ���ʵ�ֵ�ǣ�{}".format(pi))

# ����������������

DARTS = 1000*1000*10
hits = 0.0
start = time.perf_counter()
for i in range(DARTS):
	x,y = random.random(),random.random()
	dist = pow(x**2+y**2,0.5)
	if dist < 1:
		hits = hits + 1
pi = 4 * ( hits / DARTS )
print("���ؿ��޷��������Բ���ʵ�ֵ�ǣ�{}".format(pi))
print("���������ʱ���ǣ�{:.5f}s".format(time.perf_counter()-start))
