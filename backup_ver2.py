# -*- coding:utf-8 -*-
# 我想要一个可以为我的所有重要文件创建备份的程序。
# 版本2,采用更好的文件名机制,日期作为目录，时间作为名称

import os
import time

# 1. 需要备份文件的目录。
source = [r'C:\Documents']

# 2. 备份保存目录。
target_dir = 'E:\\Backup\\' #remember to change this to what you will be using

# 3. 将目标文件备份成zip格式文件。
# 4. 当前日期作为备份目录的子目录名。
today = target_dir + time.strftime('%Y%m%d')
# 时间是作为备份文件名
now = time.strftime('%H%M%S')

#如果子目录不存在，则创建子目录
if not os.path.exists(today):
	os.mkdir(today) # make directory
	print 'Successful created directory', today

#备份文件的名字
target = today + os.sep + now +'.zip' #os.sep 根据你所处的平台，自动地采用相应的分割符号。

# 5. windo下用rar命令，最好的方式是将rar命令添加到环境变量
#我的电脑右键属性-》高级-》环境变量-》系统变量-》新建
# 变量名：path
# 变量值:C:/Program Files/WinRAR;
# --变量值为WinRAR软件的安装路径 
zip_command=('rar a "%s" "%s"'%(target,''.join(source)))

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to ',target
else:
	print 'Backup FAILED'
