import os
import shutil


fname=input("enter file name: ")
dir=str(input("enter video directory path: "))
destdir=str(input("enter video destination path: "))

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content] 
accepted = [i.split(' ', 1)[0] for i in content]
content = [i.split(' ', 1)[1] for i in content]
#print(content)
#print(accepted)


i=0
for file in os.listdir(dir):
     filename = os.fsdecode(file)
     if filename.endswith(".avi") and content[i] == ' 1' : 
         print(filename)
         shutil.move(dir+"/" +accepted[i]+".avi", destdir)
         i+=1
         continue
     i+=1
     