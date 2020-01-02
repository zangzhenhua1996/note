import os
path = r'../python-web'
list1=[]
for filename in os.listdir(path):
    if filename.endswith(".md"):
        str1= '- '+ filename.replace(".md","") +': '+'python学习/'+filename
        print(str1)