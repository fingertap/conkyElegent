#coding:utf-8
#!/usr/bin/python
from CONFIGS import *
print(TEMPERATURE, end="")
if len(TEMPERATURE) < 2:
    print(' ', end="")
import shutil
target = '/home/han/.conky/weather/dummy.png'
shutil.copyfile(TARGET_FIG, target)
