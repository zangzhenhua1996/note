import os
path = r'未分类'
list1=[]
for filename in os.listdir(path):
    if filename.endswith(".md"):
        str1= '- '+ filename.replace(".md","") +': '+path+'/'+filename
        list1.append(str1)
data = list1
data.reverse()

with open("反转后.txt",'w',encoding="utf-8") as f:
    for line in data:
        f.write(line+'\n')