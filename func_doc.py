# -*- coding:utf-8 -*-

def printMax(x,y):
	'''Print the maximun of two numbers.
	
	the two values must be integers.'''
	x = int(x) # conver to integers, if possible
	y = int(y)
	
	if x > y:
		print x ,'is maximun'
	else:
		print y,'is maximum'
		
printMax(3,5)
print printMax.__doc__

# 文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。
# 第二行是空行，从第三行开始是详细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。
