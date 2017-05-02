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
