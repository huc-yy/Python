# -*- coding:utf-8 -*-

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist),'items to purchase.'

print 'These items are:', # Notice the comma at end of the line
for item in shoplist:
	print item, # 这里，我们在print语句的结尾使用了一个逗号来消除每个print语句自动打印的换行符。

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist

print 'I will sort my list now'
shoplist.sort() #对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
