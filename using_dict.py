# -*- coding:utf-8 -*-

# 'ab' is short for 'a'dress'b'ook

ab = {	'Swaroop' : 'swaroopch@byteofpython.info',
			'Larry'		: 'larry@wall.org',
			'Matsumoto' : 'matz@ruby-lang.org',
			'Spammer'	 : 'spammer@hotmail.com'
		}
		
print "Swaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name,address in ab.items(): # items() 函数以列表返回可遍历的(键, 值) 元组数组。
	print 'Contact %s at %s' % (name,address)
	
if 'Guido' in ab: # OR, ab.has_key('Guido')
	print "\nGuido's address is %s" % ab['Guido']
