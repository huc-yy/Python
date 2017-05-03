# -*- coding:utf-8 -*-

print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice the both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print 'Copy by making a full slice'
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first items

print 'shoplist is', shoplist
print 'mylist is',mylist
# notice that now the two lists are different
#如果你想要复制一个列表或者类似的序列或者其他复杂的对象（不是如整数那样的简单 对象 ），那么你必须使用切片操作符来取得拷贝。
