import os
path = r'../ubuntu系统的使用'
list1=[]
for filename in os.listdir(path):
    if filename.endswith(".md"):
        str1= '- '+ filename.replace(".md","") +': '+'ubuntu系统的使用/'+filename
        print(str1)