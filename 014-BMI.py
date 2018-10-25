#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
BMI：Body Mass INdex，国际上常用的衡量人体肥胖和健康程度的重要标准，主要用于统计分析。
定义：BMI = 体重（kg）/身高^2（m^2）

问题需求：

输入体重和身高，输出 BMI（包括国际和国内）
'''

weight,height = eval(input('输入体重(kg)和身高(m)【用,分隔】：'))
bmi = weight / pow(height,2)
print('BMI 指标为{:.1f}'.format(bmi))
who,nat = '',''
if bmi < 18.5:
	who,nat = '偏瘦','偏瘦'
elif 18.5 <= bmi < 24:
	who,nat = '正常','正常' 
elif 24 <= bmi < 25:
	who,nat = '正常','偏胖'
elif 25 <= bmi <28:
	who,nat = '偏胖','偏胖'
elif 28 <= bmi <30:
	who,nat = '偏胖','肥胖'
else:
	who,nat = '肥胖','肥胖'
print('BMI 指数，国际为{1}，国内为{0}'.format(nat,who))