# -*- coding:utf-8 -*-

import sys #从系统调用sys模块

print 'The command line arguments are:'
for i in sys.argv:
  #sys.argv变量是一个字符串列表，包含了命令行参数，即使用命令行传递给你的程序的参数。
	print i
	
print '\n\nThe PYTHONPATH is ', sys.path,'\n'

#运行 python using_sys.py 我 是 你爹
#脚本的名称总是sys.argv列表的第一个参数。
#所以，在这里，'using_sys.py'是sys.argv[0]、'我'是sys.argv[1]、'是'是sys.argv[2]以及'你爹'是sys.argv[3]。
#注意，Python从0开始计数，而非从1开始。
