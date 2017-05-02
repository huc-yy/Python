#!/usr/bin/python
# Filename: mymodule.py

def sayhi():
    print 'Hi, this is mymodule speaking.'

version = '0.1'

# End of mymodule.py

'''我们接下来将看看如何在我们别的Python程序中使用这个模块。

记住这个模块应该被放置在我们输入它的程序的同一个目录中，或者在sys.path所列目录之一。'''

#下面是另一个程序，使用先前所创模块
#!/usr/bin/python
# Filename: mymodule_demo.py

import mymodule

mymodule.sayhi()
print 'Version', mymodule.version

#下面是一个使用from..import语法的版本。
#!/usr/bin/python
# Filename: mymodule_demo2.py

from mymodule import sayhi, version
# Alternative:
# from mymodule import *

sayhi()
print 'Version', version
