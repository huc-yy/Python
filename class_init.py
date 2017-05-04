# -*- coding:utf-8 -*-

class Person:	
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print '你好，我的名字是', self.name
		
p = Person('小王')
p.sayHi()

"""这里，我们把__init__方法定义为取一个参数name（以及普通的参数self）。
在这个__init__里，我们只是创建一个新的域，也称为name。注意它们是两个不同的变量，尽管它们有相同的名字。点号使我们能够区分它们。
最重要的是，我们没有专门调用__init__方法，只是在创建一个类的新实例的时候，把参数包括在圆括号内跟在类名后面，从而传递给__init__方法。"""
