# -*- coding:utf-8 -*-
# 我想要一个可以为我的所有重要文件创建备份的程序。
""" 版本3,备份文件归档命名由用户提供备注，当然，下个版本可以继续更新用户自己输入要备份
的路径，以及想保存的目录路径，再图形化。"""

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

#从用户那获取名称备注
comment = raw_input('请输入你想给文件备注的名字：')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now +'_'+\  #反斜杠表示逻辑行在下一物理行继续
		comment.replace(' ', '_') + '.zip'

#如果子目录不存在，则创建子目录
if not os.path.exists(today):
	os.mkdir(today) # make directory
	print 'Successful created directory', today

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
