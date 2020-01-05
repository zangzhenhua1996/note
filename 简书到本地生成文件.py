# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:28:06 2020

@author: zangz
"""


import os
path = r'mysql8-0使用'
list1=[]
for filename in os.listdir(path):
    if filename.endswith(".md"):
        str1=filename
        list1.append(str1)
data = list1
data.reverse()
for line in data:
    line = 'mysql8-0使用'+'/'+line
    with open(line,'w',encoding="utf-8") as f:
        f.write(line)