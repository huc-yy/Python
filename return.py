# -*- coding:utf-8 -*-
def maximum(x,y):
	if x > y:
		return x 
	else:
		return y 

x,y = map(int,raw_input('请输入要比较大小的两个数，以逗号隔开（例：2,3）：').split(','))
print 'maximum is',maximum(x,y)
