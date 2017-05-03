# -*- coding:utf-8 -*-

name = 'Swaroop' # This is a string object

if name.startswith('Swa'): #startwith方法是用来测试字符串是否以给定字符串开始。
	print 'Yes, the string starts with "Swa"'
	
if 'a' in name:
	print 'Yes, it contains the string "a"'
	
if name.find('war') != -1: #find方法用来找出给定字符串在另一个字符串中的位置，或者返回-1以表示找不到子字符串。
	print 'Yes, it contains the string "war"'
	
delimiter = '_*_'
mylist = ['Brazi', 'Russia', 'India', 'China']
print delimiter.join(mylist) #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
