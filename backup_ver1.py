# -*- coding:utf-8 -*-
# 我想要一个可以为我的所有重要文件创建备份的程序。
# 版本1

import os
import time

# 1. 需要备份文件的目录。
source = [r'C:\Documents']

# 2. 备份保存目录。
target_dir = 'E:\\Backup\\' #remember to change this to what you will be using

# 3. 将目标文件备份成zip格式文件。
# 4. zip备份文件的名称是当前的日期和时间。
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'

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
