#!/usr/bin/python
FHW=open("data.txt","w")
FHW.write("written some thing")
print(FHW.tell())
print("closed?",FHW.closed)
FHW.close()
print("after closing the file closed?",FHW.closed)
