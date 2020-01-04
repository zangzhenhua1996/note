import os
path = r'力扣刷题'
list1=[]
for filename in os.listdir(path):
    if filename.endswith(".md"):
        str1= '- '+ filename.replace(".md","") +': '+'力扣刷题/'+filename
        list1.append(str1)
data = list1
data.reverse()

with open("反转后.txt",'w',encoding="utf-8") as f:
    for line in data:
        f.write(line+'\n')